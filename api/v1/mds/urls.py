from django.conf.urls import patterns, url
from api.v1.mds.views import *


urlpatterns = patterns(
    url(r'^status/', mds_status_view),
    url(r'^dump/', mds_dump_view),
)
