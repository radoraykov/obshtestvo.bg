from django.conf.urls import patterns, include, url
from django.contrib import admin
import autocomplete_light
from web.views import home, wip, about, project, support, members, contact, faq, report
autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', home.HomeView.as_view(), name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^wip\.html$', wip.WipView.as_view(), name='wip'),
                       url(r'^about\.html$', about.AboutView.as_view(), name='about'),
                       url(r'^report\.html$', report.ReportView.as_view(), name='report'),
                       url(r'^faq\.html$', faq.FaqView.as_view(), name='faq'),
                       url(r'^support\.html$', support.SupportView.as_view(),
                           name='support'),
                       url(r'^members$', members.MembersView.as_view(), name='members'),
                       url(r'^contact$', contact.ContactView.as_view(), name='contact'),
                       url(r'^project/(?P<name>[^/]+)\.html$',
                           project.ProjectView.as_view(),
                           name='project'),
)
