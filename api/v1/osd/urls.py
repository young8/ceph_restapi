from django.conf.urls import patterns, url
from api.v1.osd.views import *


urlpatterns = patterns(
    '',
    url(r'^list/', osd_list_view),
    url(r'^lstree/', osd_ls_tree_view),
    url(r'^lscrush/', osd_ls_crush_view),
    url(r'^lspool/', osd_ls_pool_view),
    url(r'^status/', osd_performance_view),
    url(r'^action/up/(?P<id>\d+)/$', action_in),
    url(r'^action/out/(?P<id>\d+)/$', action_out),
    url(r'^action/down/(?P<id>\d+)/$', action_down),
)
