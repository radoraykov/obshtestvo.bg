from django.views.generic.base import View
from restful.decorators import restful_view_templates
from django.conf import settings


@restful_view_templates
class SupportView(View):
    def get(self, request):
        return {
            "page": "inner support",
            "projects": settings.FAKE_DB,
            "selectedProject": request.params.get('project'),
            "positions": settings.MEMBER_POSITIONS
        }