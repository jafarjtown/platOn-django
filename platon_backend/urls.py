
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
def Index(request):
    return render(request, 'index.html')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('api/account/', include('account.urls')),
    path('api/courses/', include('course.urls')),
    path('api/tutorials/', include('community.urls')),
]
