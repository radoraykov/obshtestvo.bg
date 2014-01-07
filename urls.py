from django.conf.urls import patterns, include, url

from web.views import home, wip

urlpatterns = patterns('',
                       url(r'^$', home.HomeView.as_view(), name='home'),
                       url(r'^wip\.html$', wip.WipView.as_view(), name='wip'),
)
