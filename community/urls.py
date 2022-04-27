from django.urls import path
from . import views
app_name = 'community'
urlpatterns = [
    path('', views.TutorialAPIView.as_view(), name='tutorial_api_view')
]