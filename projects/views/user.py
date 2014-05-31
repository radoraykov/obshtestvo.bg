from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from restful.decorators import restful_view_templates
from guardian.decorators import permission_required_or_403

from projects.models import Project, User


@restful_view_templates
class UserView(View):

    @method_decorator(login_required)
    @method_decorator(permission_required_or_403('projects.change_user', (User, 'id', 'id')))
    def put(self, request, id):
        user = User.objects.get(pk=id)
        current_ids = list(User.objects.filter(pk=id).values_list('projects_interests__id', flat=True))
        project_ids = list(Project.objects.values_list('id', flat=True))
        ProjectLinkModel = User.projects_interests.through
        links = []
        for id in request.params.get('projects', []):
            id = int(id)
            if id in current_ids:
                current_ids.remove(id)
            else:
                if id in project_ids:
                    links.append(ProjectLinkModel(user_id=user.id, project_id=id))

        if filter(None, current_ids):
            ProjectLinkModel.objects.filter(project_id__in=current_ids).delete()
        if links:
            ProjectLinkModel.objects.bulk_create(links)