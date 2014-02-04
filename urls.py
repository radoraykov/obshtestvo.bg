from django.conf.urls import patterns, url

from web.views import home, wip, about, project, support, members, contact

urlpatterns = patterns('',
                       url(r'^$', home.HomeView.as_view(), name='home'),
                       url(r'^wip\.html$', wip.WipView.as_view(), name='wip'),
                       url(r'^about\.html$', about.AboutView.as_view(), name='about'),
                       url(r'^support\.html$', support.SupportView.as_view(),
                           name='support'),
                       url(r'^members$', members.MembersView.as_view(), name='members'),
                       url(r'^contact$', contact.ContactView.as_view(), name='contact'),
                       url(r'^project/(?P<name>[^/]+)\.html$',
                           project.ProjectView.as_view(),
                           name='project'),
)
