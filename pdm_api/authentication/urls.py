from django.urls import path
from .views import RegisterView, LoginView, UserListView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('users', UserListView.as_view(), name='users'),
]