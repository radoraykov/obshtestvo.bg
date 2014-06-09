from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import home, wip, about, project, support, members, contact, faq, report
from login.views import login
from auth.views import extra_data, entry
from projects.views import dashboard, user, users
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home.HomeView.as_view(), name='home'),
    url(r'', include('auth.urls', namespace='social')),
    url(r'^logout/$', entry.LogoutView.as_view(), name='logout'),

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

    url(r'^extradata/$', extra_data.ExtraDataView.as_view(), name='require_extra_data'),

    url(r'^join/$', login.LoginView.as_view()),

    url(r'^user/(?P<id>\d+)', user.UserView.as_view(), name='user'),
    url(r'^user/profile/(?P<id>\d+)$', user.UserProfileView.as_view(), name='user-profile'),

    url(r'^users/$', users.UsersView.as_view(), name='users'),

    url(r'^dashboard/$', dashboard.DashboardView.as_view(), name='dash'),

)
