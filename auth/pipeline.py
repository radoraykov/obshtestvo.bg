from django.shortcuts import redirect

from social.pipeline.partial import partial
from social.exceptions import AuthException


@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if user and user.email and user.crazy_field:
        return
    elif not details.get('email') or not details.get('crazy_field'):
        if strategy.session_get('saved_email'):
            details['email'] = strategy.session_pop('saved_email')
            details['first_name'] = strategy.session_pop('saved_first_name')
            details['crazy_field'] = strategy.session_pop('saved_crazy_field')
        else:
            return redirect('require_email')


def user_password(strategy, request, user=None, is_new=False, *args, **kwargs):
    if strategy.backend.name != 'email':
        return

    password = request.params.get('password')
    if is_new:
        user.set_password(password)
        user.save()
    elif not user.validate_password(password):
        # return {'user': None, 'social': None}
        raise AuthException(strategy.backend)