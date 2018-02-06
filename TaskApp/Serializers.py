from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'first', 'last', 'password')
        extra_kwargs = {
            'url': {'view_name': 'UsersViewSet', 'lookup_field': 'id'}
        }