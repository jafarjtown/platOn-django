from django.urls import path
from . import views
app_name = 'community'
urlpatterns = [
    path('event/all/', views.EventAllAPIView.as_view(), name='event_all_api'),
    path('event/', views.EventAPIView.as_view(), name='event_api'),
]