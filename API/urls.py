

from django.urls import path, include

urlpatterns = [
    path('tutorial/', include('tutorial.urls')),
    path('article/', include('Article.urls')),
    path('solution/', include('Solution.urls')),
    path('account/', include('account.urls')),
]

