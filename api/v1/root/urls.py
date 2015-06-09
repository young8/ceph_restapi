from django.conf.urls import patterns, url
from api.v1.root.views import *


urlpatterns = patterns(
    '',
    url(r'^fsid/', cluster_list),
    url(r'^df/', cluster_df),
    url(r'^health/', cluster_health),
    url(r'^status/', cluster_status),
    url(r'^fs/', cluster_file_sysyem),
    url(r'^performance/', cluster_performance),
)
