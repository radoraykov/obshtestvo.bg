from django.shortcuts import redirect
from projects.models import User, Skill

from social.pipeline.partial import partial
from social.exceptions import AuthException


@partial
def require_extra_data(strategy, details, user=None, is_new=False, *args, **kwargs):
    if not is_new:
        return

    if strategy.session_get('saved_email'):
        details['available_after'] = strategy.session_pop('saved_available_after')
        details['email'] = strategy.session_pop('saved_email')
        name = strategy.session_pop('saved_name').split(' ', 1)
        details['first_name'] = name[0]
        details['last_name'] = name[1]

    else:
        return redirect('require_extra_data')


def save_extra_data(strategy, user=None, is_new=False, *args, **kwargs):
    if not is_new:
        return

    submitted_ids = strategy.session_pop('saved_skills').split('|')
    existing_ids = Skill.objects.values_list('id', flat=True)
    ids = []

    for id in submitted_ids:
        if id.isdigit():
            id = int(id)
            if id in existing_ids:
                ids.append(id)
        else:
            s = Skill()
            s.name = id
            s.save()
            ids.append(s.id)

    links = []
    LinkModel = User.skills.through
    for id in ids:
        links.append(LinkModel(user_id=user.id, skill_id=id))

    LinkModel.objects.bulk_create(links)


def user_password(strategy, request, user=None, is_new=False, *args, **kwargs):
    if not (strategy.backend.name == 'email' or strategy.backend.name == 'username'):
        return

    password = request.params.get('password')
    if is_new:
        user.set_password(password)
        user.save()
    elif not user.check_password(password):
        return {'user': None, 'social': None}
        # raise AuthException(strategy.backend)


def load_user(strategy, request, user=None, is_new=False, *args, **kwargs):
    try:
        return {
            "user": User.objects.get(username=request.params.get('username'))
        }
    except Exception:
        return None