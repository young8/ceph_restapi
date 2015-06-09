from django.conf.urls import patterns, include, url



urlpatterns = patterns(
    '',
    url(r'^cluster/', include('api.v1.root.urls')),
    url(r'^osd/', include('api.v1.osd.urls')),
    url(r'^mon/', include('api.v1.mon.urls')),
    url(r'^pool/', include('api.v1.pool.urls')),
    url(r'^pgs/', include('api.v1.pgs.urls')),
    url(r'^mds/', include('api.v1.mds.urls')),
)
