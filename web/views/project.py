from django.conf import settings
from django.views.generic.base import View
from restful.decorators import restful_view_templates


@restful_view_templates('project')
class ProjectView(View):
    def get(self, request, name):
        project = settings.FAKE_DB[name]
        return {
            "page": "inner project",
            "project": project,
            "positions": settings.MEMBER_POSITIONS
        }
