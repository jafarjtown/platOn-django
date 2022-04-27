
from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

app_name = 'account'
urlpatterns = [
    path('user/', views.UserAPIView.as_view(), name='user_login'),
    path('user/new/', views.UserCreateAPI.as_view(), name='user_create'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
 
]
   