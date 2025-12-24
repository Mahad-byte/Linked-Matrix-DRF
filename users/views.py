import requests
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = get_user_model()
        response = user.objects.create_user(email=email, password=password)
        print(response)

        return Response(f"User Created!: {response}, Please Login to Proceed")
    
    def get(self, request):
        return Response("Okay In Get!!!!!")
    

class LoginView(APIView):
    serializer_class = UserSerializer
    def get(self, request):
        return Response("Okay In Get!!!!!")
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        print(user, email, password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=401)
        
        # data = {
        # 'email':email,
        # 'password':password
        # }
        # access_token = requests.post('http://127.0.0.1:8000/api/token/', json=data)
        # print(access_token.json())
        # token_data = access_token.json()
    
        # header = {
        #     "Authorization": f"Bearer {token_data['access']}"
        # }
        
        # token_request = requests.post('http://127.0.0.1:8000/api/token/', json=data, headers=header)
        # if token_request:
        #     return Response("Home")
        
        refresh = RefreshToken.for_user(user)
        home_data = {
                    "message": "Welcome Home",
                    "user": user.email,
                }

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "home":home_data
        })

        
class LogoutView(APIView):
    def get(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Logout Succedded")
        