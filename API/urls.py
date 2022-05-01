

from django.urls import path, include

urlpatterns = [
    # path('tutorial/', include('Tutorial.urls')),
    path('article/', include('Article.urls')),
    path('solution/', include('Solution.urls')),
    path('account/', include('account.urls')),
]

