from django.conf.urls import patterns, url
from views import entry

urlpatterns = patterns('',
    # authentication / association
    url(r'^login/(?P<backend>[^/]+)/$', entry.CredentialsView.as_view(),
        name='begin'),
    url(r'^token/(?P<backend>[^/]+)/', entry.TokenView.as_view(), name='token'),
    url(r'^complete/(?P<backend>[^/]+)/$', entry.RegisterView.as_view(),
        name='complete'),
)
