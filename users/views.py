from rest_framework.views import APIView
from rest_framework.response import Response

class GoogleLogin(APIView):
    def post(self, request):
        return Response(request.data, status=200)
       