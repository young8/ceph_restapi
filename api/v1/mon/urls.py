from django.conf.urls import patterns, url
from api.v1.mon.views import *


urlpatterns = patterns(
    '',
    url(r'^list/', mon_list_view),
)
