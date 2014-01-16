from django.conf.urls import patterns, url

from web.views import home, wip, about, knowyourmp

urlpatterns = patterns('',
                       url(r'^$', home.HomeView.as_view(), name='home'),
                       url(r'^wip\.html$', wip.WipView.as_view(), name='wip'),
                       url(r'^about\.html$', about.AboutView.as_view(), name='about'),
                       url(r'^project\.html$', knowyourmp.KnowYourMpView.as_view(),
                           name='project'),
)
