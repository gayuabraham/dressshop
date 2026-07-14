from rest_framework import serializers
from .models import item
from django.contrib.auth.models import User

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
        read_only_fields = 'user'

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username' , 'password' , 'email']

    def create(self , validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email = validated_data['email'],
            password= validated_data['password']
        )
        return user


     
        
        