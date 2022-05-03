from django.urls import path
from . import views

urlpatterns = [
    path('', views.TutorialAPIView.as_view(), name='tutorial_api_view'),
    path("cover_image/<int:pk>", views.TutorialAPIView.as_view(), name="tutorial_image_view"),
]