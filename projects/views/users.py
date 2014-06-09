from django.views.generic.base import View

from restful.decorators import restful_view_templates

from projects.models import SkillGroup
from projects.services import SkillPickerService

@restful_view_templates
class UsersView(View):

    def get(self, request):
        return {
            'skills_options': SkillPickerService().all()
        }