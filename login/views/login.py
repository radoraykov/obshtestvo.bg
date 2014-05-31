from django.views.generic.base import View
from django.shortcuts import redirect

from restful.decorators import restful_view_templates
from projects.models import Project

@restful_view_templates
class LoginView(View):
    # user.social_user
    # user.get_profile().profile_photo.save('{0}_social.jpg'.format(user.username), ContentFile(response.content)); profile.save()
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('dash')

        return {
            "page": "inner entry",
            "projects": Project.objects.all(),
        }