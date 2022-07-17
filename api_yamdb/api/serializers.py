from reviews.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    role = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('role', 'bio', 'email', 'username', 'first_name',
                  'last_name')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Имя me нельзя использовать')
        return value


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('role', 'bio', 'email', 'username', 'first_name',
                  'last_name')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Имя me нельзя использовать')
        return value


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Имя me нельзя использовать')
        return value


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
