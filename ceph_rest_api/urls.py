from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet
from api.v1.root.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('api.v1.urls')),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
