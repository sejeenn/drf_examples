from rest_framework import serializers
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model

User = get_user_model()


def phone_validate_func(phone_number):
    if len(phone_number) != 10:
        raise serializers.ValidationError(
            'Длина телефона должна быть равна 10 символам'
        )


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()
    phone = serializers.CharField(required=False)

    def validate_email(self, value):
        if value is None:
            return value

    def validate_username(self, value):
        print('validate_username', value)
        if value is None:
            return value

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким username уже существует"
            )
        return value

    def validate(self, attrs):
        email, username = attrs.get('email', None), attrs.get('username', None)
        if email is None and username is None:
            raise serializers.ValidationError(
                {
                    api_settings.NON_FIELD_ERRORS_KEY:
                        "Необходимо указать либо email либо username"
                }
            )
        if username is None:
            attrs['username'] = email
        if email is None:
            attrs['email'] = username + '@anymail.ru'
        return attrs

    def create(self, validated_data):
        User.objects.create(**validated_data)



