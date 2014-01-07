from django.conf.urls import patterns, include, url

from web.views import home

urlpatterns = patterns('',
                       url(r'^$', home.HomeView.as_view(), name='home'),
)
