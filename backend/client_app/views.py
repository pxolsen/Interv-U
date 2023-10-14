from .models import Client
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class User_permissions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class Sign_up(APIView):
    def post(self, request):
        request.data["username"] = request.data["email"]
        client = Client.objects.create_user(**request.data)
        token = Token.objects.create(user=client)
        return Response(
            {"client": client.email, "token": token.key}, status=HTTP_201_CREATED
        )
        
class Log_in(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        client = authenticate(username=email, password=password)
        if client:
            token, created = Token.objects.get_or_create(user=client)
            return Response({"token": token.key, "client": client.email})
        else:
            return Response("No user matching credentials", status=HTTP_404_NOT_FOUND)

class Info(User_permissions):
    def get(self, request):
        return Response({"email": request.user.email})
    
class Log_out(User_permissions):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Master_Sign_Up(APIView):
    def post(self, request):
        request.data["username"] = request.data["email"]
        master_client = Client.objects.create_user(**request.data)
        master_client.is_staff = True
        master_client.is_superuser = True
        master_client.save()
        token = Token.objects.create(user=master_client)
        return Response(
            {"master_client": master_client.email, "token": token.key}, status=HTTP_201_CREATED
        )

class Delete(User_permissions):
    def delete(self, request):
        request.user.delete()
        return Response(status=HTTP_204_NO_CONTENT)