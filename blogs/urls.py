from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="post_detail"),
]