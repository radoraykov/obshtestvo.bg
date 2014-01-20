from django.conf.urls import patterns, url

from web.views import home, wip, about, project, members

urlpatterns = patterns('',
                       url(r'^$', home.HomeView.as_view(), name='home'),
                       url(r'^wip\.html$', wip.WipView.as_view(), name='wip'),
                       url(r'^about\.html$', about.AboutView.as_view(), name='about'),
                       url(r'^members$', members.MembersView.as_view(), name='members'),
                       url(r'^project/(?P<name>[^/]+)\.html$',
                           project.ProjectView.as_view(),
                           name='project'),
)
