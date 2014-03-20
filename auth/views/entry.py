from django.views.generic.base import View
from restful.decorators import restful_view_templates
from django.http.response import HttpResponseRedirectBase
from social.apps.django_app.views import auth, complete, _do_login as login
from django.contrib.auth import logout
from django.shortcuts import redirect
from social.apps.django_app.utils import load_strategy, strategy
from django.utils.decorators import method_decorator

@restful_view_templates
class CredentialsView(View):
    def get(self, request, backend):
        return auth(request, backend)

# to be mainly accessed by AJAX
@restful_view_templates
class TokenView(View):

    @method_decorator(strategy)
    def post(self, request, backend):
        stra = load_strategy(request=request, backend=backend)
        auth_result = stra.backend.do_auth(
            access_token=request.POST['auth_token'],
            user=request.user.is_authenticated() and request.user or None
        )
        if request.is_ajax() and isinstance(auth_result, HttpResponseRedirectBase):
            return {
                "redirect": auth_result.url
            }, 202
        else:
            login(stra, auth_result)

@restful_view_templates
class RegisterView(View):
    def get(self, request, backend, *args, **kwargs):
        return complete(request, backend, *args, **kwargs)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


@restful_view_templates
class ValidationSentView(View):
    def get(self, request):
        return {
             'email': request.session.get('email_validation_address')
        }
