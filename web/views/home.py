from django.views.generic.base import View
from restful.decorators import restful_view_templates


@restful_view_templates('home')
class HomeView(View):
    def get(self, request):
        return {
            "page": "home",
            "page": "home",
        }
