from django.views.generic.base import View
from restful.decorators import restful_view_templates
from django.conf import settings


@restful_view_templates('support')
class SupportView(View):
    def get(self, request):
        return {
            "page": "inner about support",
            "projects": settings.FAKE_DB,
            "positions": settings.MEMBER_POSITIONS
        }