from django.urls import path, include
from post.views import PostViewset, LoginView, RegisterView, RegisterAPIView
from rest_framework.routers import DefaultRouter
# from api.views import LoginView, RegisterView, PostCreateView

router = DefaultRouter()

router.register(r'post',PostViewset, basename="post"),
# router.register(r'post/list',PostViewset, basename="post"),
# router.register(r'post/create',PostViewset, basename="create"),
# router.register(r'post/delete/<int:pk>/',PostViewset, basename="delete"),
# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('post/update/<int:pk>/', RegisterAPIView.as_view(), name='update'),
    # path('post/create/', PostCreateView.as_view(), name='create'),
]