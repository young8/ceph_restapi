from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *


@api_view(['GET'])
def osd_list_view(request):
    return Response(staticModel.osd())


@api_view(['GET'])
def osd_performance_view(request):
    return Response(staticModel.performance())


@api_view(['GET'])
def osd_ls_tree_view(request):
    return Response(staticModel.lstree())


@api_view(['GET'])
def osd_ls_crush_view(request):
    return Response(staticModel.lscrush())


@api_view(['GET'])
def osd_ls_pool_view(request):
    return Response(staticModel.lspool())


# PUT Method
@api_view(['PUT'])
def action_in(request, id):
    print id
    return Response(staticModel.osd_in(id))


@api_view(['PUT'])
def action_out(request, id):
    return Response(staticModel.osd_out(id))


@api_view(['PUT'])
def action_down(request, id):
    return Response(staticModel.osd_down(id))
