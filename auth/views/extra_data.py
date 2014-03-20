from django.views.generic.base import View
from restful.decorators import restful_view_templates
from django.shortcuts import redirect


@restful_view_templates
class ExtraDataView(View):
    def get(self, request):
        return {
            'details': request.session['partial_pipeline']['kwargs']['details']
        }

    def post(self, request):
        request.session['saved_email'] = request.params.get('email')
        request.session['saved_first_name'] = request.params.get('first_name')
        request.session['saved_crazy_field'] = request.params.get('crazy_field')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)