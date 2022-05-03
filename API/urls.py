

from django.urls import path, include

urlpatterns = [
    path('tutorial/', include('tutorial.urls')),
    path('article/', include('Article.urls')),
    path('account/', include('account.urls')),
]

