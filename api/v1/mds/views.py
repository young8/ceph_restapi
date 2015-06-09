from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *


@api_view(['GET'])
def mds_status_view(request):
    return Response(staticModel.mds_status())


@api_view(['GET'])
def mds_dump_view(request):
    return Response(staticModel.mds_dump())


# PUT Method


