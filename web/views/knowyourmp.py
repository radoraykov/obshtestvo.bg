from django.views.generic.base import View
from restful.decorators import restful_view_templates


@restful_view_templates('knowyourmp')
class KnowYourMpView(View):
    def get(self, request):
        return {
            "page": "inner project",
        }
