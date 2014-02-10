from django.views.generic.base import View
from restful.decorators import restful_view_templates


@restful_view_templates('report')
class ReportView(View):
    def get(self, request):
        return {
            "page": "inner report",
        }
