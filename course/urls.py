from django.urls import path
from . import views
app_name = 'course'
urlpatterns = [
    path('', views.Courses.as_view(), name='get_courses')
]
