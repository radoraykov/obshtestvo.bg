from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from restful.decorators import restful_view_templates
from projects.models import Project


@restful_view_templates
class DashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        return {
            "page": "inner dash",
            "projects": Project.objects.select_related('interested_users').all(),
        }