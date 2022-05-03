

from django.urls import path, include

urlpatterns = [
    path('community/', include('community.urls')),
    path('article/', include('Article.urls')),
    path('solution/', include('Solution.urls')),
    path('account/', include('account.urls')),
]

