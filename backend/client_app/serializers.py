from rest_framework.serializers import ModelSerializer
# from django.contrib.auth import get_user_model
from .models import Client

class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ["id", "email", "first_name", "last_name", "profile_pic"]