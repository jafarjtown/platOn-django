from django.urls import path
from . import views
app_name = 'solution'
urlpatterns = [
    path('', views.SolutionListAPIView.as_view(), name='solution'),
    path('new/', views.SolutionCreateAPIView.as_view(), name='solution_create'),
    path('update/<int:pk>/', views.SolutionUpdateAPIView.as_view(), name='solution_update'),
    path('<int:pk>/', views.SolutionDetailDeleteAPIView.as_view(), name='solution_detail_delete'),
]