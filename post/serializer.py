from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True) 
    username = serializers.CharField(required=True)
    password =  serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email','username','password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    class meta:
        model = User
        fields = ['email']

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True,min_length=2)
    class meta:
        model = User
        fields = ['password']

    def validate(self, data):
        password = data.get("password")
        token = self.context.get("kwargs").get(token)
        encoded_pk = self.context.get("kwargs").get(encoded_pk)
        if token is None or encoded_pk is None:
            serializers.ValidationError("Missing Data")
        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator(user, token):
            raise serializers.ValidationError("The reset token is Invalid")
        user.set_password(password)
        user.save()
        return data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"