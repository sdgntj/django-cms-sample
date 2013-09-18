from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

urlpatterns = patterns('account.views',
    url(r'^ajax-login/$', 'ajax_login_view', name="ajax_login"),
    url(r'^logout/$', logout, name="logout", kwargs={'next_page': '/'}),
    url(r'^action/(?P<action>[^/]+)/', 'action_view')
)
