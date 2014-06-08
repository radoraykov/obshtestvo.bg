from django.views.generic.base import View

from restful.decorators import restful_view_templates

@restful_view_templates
class UsersView(View):

    def get(self, request):
        pass