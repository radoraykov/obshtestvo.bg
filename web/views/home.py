from django.conf import settings
from django.views.generic.base import View
from restful.decorators import restful_view_templates

@restful_view_templates
class HomeView(View):
    def get(self, request):
        return {
            "page": "home",
            "projects": settings.FAKE_DB,
        }
