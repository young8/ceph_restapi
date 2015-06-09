from api.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def cluster_list(request):
    return Response(staticModel.cluster_ids())


@api_view(['GET'])
def cluster_df(request):
    return Response(staticModel.df())


@api_view(['GET'])
def cluster_file_sysyem(request):
    return Response(staticModel.fs())


@api_view(['GET'])
def cluster_health(request):
    return Response(staticModel.health())


@api_view(['GET'])
def cluster_status(request):
    return Response(staticModel.status())


@api_view(['GET'])
def cluster_performance(request):
    return Response(staticModel.performance())