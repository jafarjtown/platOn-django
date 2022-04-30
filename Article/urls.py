from django.urls import path
from . import views
app_name = 'tutorial'
urlpatterns = [
    path('', views.ArticleListAPIView.as_view(), name='articles'),
    path('new/', views.ArticleCreateAPIView.as_view(), name='article_create'),
    path('update/<int:pk>/', views.ArticleUpdateAPIView.as_view(), name='article_update'),
    path('<int:pk>/', views.ArtileDetailDeleteAPIView.as_view(), name='article_detail_delete'),
]