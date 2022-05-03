

from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('community/', include('community.urls')),
=======
    path('tutorial/', include('tutorial.urls')),
>>>>>>> 76469c629f9f22df8ca70c911aa718f919f26dff
    path('article/', include('Article.urls')),
    path('solution/', include('Solution.urls')),
    path('account/', include('account.urls')),
]

