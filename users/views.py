from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response("Okay In Get!!!!!")
    

class LoginView(APIView):
    serializer_class = LoginSerializer
    def get(self, request):
        return Response("Okay In Get!!!!!")
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response({
                'refresh': data['refresh'],
                'access': data['access'],
                'user': data['user'].email,
            })
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

        
class LogoutView(APIView):
    def get(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Logout Succedded")
        