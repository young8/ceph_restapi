from django.conf.urls import patterns, url
from api.v1.pgs.views import *


urlpatterns = patterns(
    '',
    url(r'^status/', pgs_status_view),
    url(r'^dump/', pgs_dump_view),
    url(r'^set_full_ratio/(?P<ration>[\d].[\d])/$', pool_full_ration),
    url(r'^set_nearfull_ratio/(?P<ration>[\d].[\d])/$', pool_nearfull_ration),
)
