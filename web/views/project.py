# coding: utf-8
from django.conf import settings
from django.views.generic.base import View
from web.views import read_markdown
from restful.decorators import restful_view_templates
import os


@restful_view_templates('project')
class ProjectView(View):
    def get(self, request, name):
        project = settings.FAKE_DB[name]
        description_path = os.path.join(os.path.dirname(__file__),
                                        '../templates/project/fakedb/_' + project[
                                            "slug"] + '.md')
        return {
            "page": "inner project",
            "description": read_markdown(description_path),
            "project": project,
            "positions": settings.MEMBER_POSITIONS
        }
