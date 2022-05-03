from django.urls import path
from . import views

urlpatterns = [
    path("", views.TutorialListAPIView.as_view(), name="tutorials"),
    path("create", views.TutorialCreateAPIView.as_view(), name="tutorial_create"),
    path("update/<int:pk>", views.TutorialUpdateAPIView.as_view(), name="tutorial_update"),
    path("update_image/<int:pk>", views.TutorialUpdateImageAPIView.as_view(), name="tutorial_update_image"),
    path("delete/<int:pk>", views.TutorialDeleteAPIView.as_view(), name="tutorial_delete"),

    path("review", views.TutorialReveiw.as_view(), name="tutorial_review"),
    path("review_image", views.TutorialReveiwImage.as_view(), name="tutorial_review_image"),
]