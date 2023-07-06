from django.urls import path, include
from post.views import PostViewset, LoginView, RegisterView, RegisterAPIView, ResetPasswordView, PasswordReset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"post",PostViewset, basename="post"),
# router.register(r'post/list',PostViewset, basename="post"),
# router.register(r'post/create',PostViewset, basename="create"),
# router.register(r'post/delete/<int:pk>/',PostViewset, basename="delete"),
# urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("update/<int:pk>/", RegisterAPIView.as_view(), name="update"),
    path("change-password/", ResetPasswordView.as_view(), name="change-password"),
    path("password_reset/", include('django_rest_passwordreset.urls', namespace="password_reset")),
    path("password-reset/",ResetPasswordView.as_view(),
         name="reset-password"
         ),
    path("password-reset/<str:encoded_pk>/<str:token>/",PasswordReset.as_view(),
         name="reset-password"
         )
]
