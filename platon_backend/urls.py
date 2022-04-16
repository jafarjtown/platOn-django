
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
def Index(request):
    return HttpResponse('<h1>PlatON Server</h1> <br/> <p>welcome to our server</p>')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('api/account/', include('account.urls')),
    path('api/courses/', include('course.urls'))
]
