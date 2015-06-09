from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *


@api_view(['GET'])
def mon_list_view(request):
    return Response(staticModel.mon_list())

