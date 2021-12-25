from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import get_user_model



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
#
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model=User
#         fields = ['id', 'username', 'email', 'password', ]

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 5:
            raise exceptions.ValidationError('Пароль слишком короткий')
        elif len(value) > 20:
            raise exceptions.ValidationError('Пароль слишком много символов')
        return value