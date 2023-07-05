from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from post.serializer import PostSerializer, UserSerializer
from post.models import Post
from django.contrib.auth import authenticate, login
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     data = request.data

    #     if "user" not in data:
    #         return JsonResponse(
    #             {"error": "Missing 'user' field in the request data"},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    #     username = data["user"]
    #     try:
    #         # Retrieve the User object
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return JsonResponse(
    #             {"error": f"User with username '{username}' does not exist"},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )
    #     post_title = data["post_title"]
    #     post_details = data["post_details"]
        
    #     user = User.objects.get(username=username)
    #     blog_post = Post.objects.create(
    #         user = user,
    #         post_title = post_title,
    #         post_details = post_details
    #     )
    #     return JsonResponse(
    #             {
    #                 "message": "Post Created successfully"
    #             },status=status.HTTP_201_CREATED,
    #         )
    
    # def destroy(self, request, pk=None):
    #     post = Post.objects.get(id=pk)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password = password)
        if user:
            login(request, user)
            return JsonResponse(
                {
                    "message": "Login successful"
                },status=status.HTTP_200_OK,
            )
        return JsonResponse(
                {
                    "message": "Invalid Credentials"
                },status=status.HTTP_401_UNAUTHORIZED
            )

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return JsonResponse(
                {
                    "message": "Registration successful"
                },status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
                {
                    "message": "Invalid Credentials"
                },serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )

class RegisterAPIView(APIView):
    def put(self, request, pk, format=None):
        # data = request.data

        # username = data["username"]
        # email = data["email"]
        # first_name = data["first_name"]
        # last_name = data["last_name"]

        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        # if user.exists():
        #     user.username = username
        #     user.email = email
        #     user.first_name = first_name
        #     user.last_name = last_name
        #     user.save()
            return JsonResponse(
                    serializer.data,status=status.HTTP_200_OK,
                )
        return JsonResponse(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )



    

    
# class PostCreateView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



