from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import ModelForm

from restful.decorators import restful_view_templates
from guardian.decorators import permission_required_or_403

from projects.models import Project, User
from projects.services import SkillPickerService
from restful.shortcuts import get_updated_data


@restful_view_templates
class UserView(View):
    @method_decorator(login_required)
    @method_decorator(permission_required_or_403('projects.change_user', (User, 'id', 'id')))
    def put(self, request, id):
        user = User.objects.get(pk=id)
        form = UserModelForm(get_updated_data(user, request.params), instance=user)

        raise Exception("TODO::manage select2 interactions for skills")

        status = 400
        if form.isValid():
            try:
                form.save()
                status = 200
            except:
                pass

        return {"status": status}, status  # more status plz


@restful_view_templates
class UserProfileView(View):
    @method_decorator(login_required)
    @method_decorator(permission_required_or_403('projects.change_user', (User, 'id', 'id')))
    def get(self, request, id):
        user = User.objects.select_related('skills').get(pk=id)
        skills = SkillPickerService().all()

        return {"user": user,
                "all_skills": skills
        }


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']