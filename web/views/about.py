from django.views.generic.base import View
from restful.decorators import restful_view_templates


@restful_view_templates
class AboutView(View):
    def get(self, request):
        return {
            "page": "inner about",
        }
