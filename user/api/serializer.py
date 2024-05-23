from rest_framework import serializers
#from user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
 class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name')