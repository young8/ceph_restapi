from django.conf.urls import patterns, url
from api.v1.pool.views import *


urlpatterns = patterns(
    url(r'^list/', pool_list_view),

)
