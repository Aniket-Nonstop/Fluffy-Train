from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post

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
    
    # def update(self, validated_data, instance):
    #     instance.username = validated_data['username',instance.username]
    #     instance.email = validated_data['email', instance.email]
    #     instance.save()
    #     return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"