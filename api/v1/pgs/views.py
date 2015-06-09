from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *


@api_view(['GET'])
def pgs_status_view(request):
    return Response(staticModel.pg_status())


@api_view(['GET'])
def pgs_dump_view(request):
    return Response(staticModel.pg_pools_dump())

# PUT Method
@api_view(['PUT'])
def pool_full_ration(request, ration):
    return Response(staticModel.set_full_ratio(ration))


@api_view(['PUT'])
def pool_nearfull_ration(request, ration):
    return Response(staticModel.set_nearfull_ratio(ration))

