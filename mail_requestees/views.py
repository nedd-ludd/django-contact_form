from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Mail_requestee
from .serializers import Mail_requesteeSerializer

class RequesteeListView(APIView):
    def get(self, _request):
      requestees = Mail_requestee.objects.all()
      serialized_requestees = Mail_requesteeSerializer(requestees, many=True)
      return Response(serialized_requestees.data, status=status.HTTP_200_OK)
    
    # def post(APIView):
    #    def post(sel)