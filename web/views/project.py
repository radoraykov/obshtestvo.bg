# coding: utf-8
from django.conf import settings
from django.views.generic.base import View
from restful.decorators import restful_view_templates
import os
from gfm import markdown


@restful_view_templates('project')
class ProjectView(View):
    def get(self, request, name):
        project = settings.FAKE_DB[name]
        description_path = os.path.join(os.path.dirname(__file__),
                                        '../templates/project/fakedb/_' + project[
                                            "slug"] + '.md')
        with open(description_path, 'r') as description_file:
            description = description_file.read().decode('utf8')
        description = markdown(description)
        return {
            "page": "inner project",
            "description": description,
            "project": project,
            "positions": settings.MEMBER_POSITIONS
        }
