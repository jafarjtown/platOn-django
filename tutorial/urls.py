from django.urls import path
from . import views

urlpatterns = [
    path("", views.TutorialCreate.as_view(), name='tutorial_create'),
    path("<int:pk>", views.TutorialCreate.as_view(), name="tutorial_create_image"),
]