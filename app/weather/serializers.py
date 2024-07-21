from rest_framework import serializers
from django.contrib.auth.models import User
from weather.models import City, UserSearchHistory


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearchHistory
        fields = '__all__'