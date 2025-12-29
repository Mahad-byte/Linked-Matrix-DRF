from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import RegisterSerializer, UserSerializer


# Create your views here.
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        print(f"Request data: {request.data}")
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("400")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response("Okay In Get!!!!!")


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get("refresh"))
        print(token)
        token.blacklist()
        return Response("Logout Succedded")
