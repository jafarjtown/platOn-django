from django.urls import path
from . import views
app_name = 'tutorial'
urlpatterns = [
    path('funcs/', views.TutorialFuncAPIView.as_view(), name='tutorial_api_view'),

    path('funcs/<int:pk>', views.TutorialFuncAPIView.as_view(), name='tutorial_api_view'),
    path('', views.TutorialListAPIView.as_view(), name='tutorial_api_view'),
]