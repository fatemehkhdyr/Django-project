from django.urls import path
from .views import ArticleListview, ArticleDtail, CategoryList,AuthorList, ArticlePriview, SearchList

app_name = "blog"
urlpatterns = [
    path('', ArticleListview.as_view(), name="home"),
    path('page/<int:page>', ArticleListview.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDtail.as_view(), name="detail"),
    path('preview/<int:pk>', ArticlePriview.as_view(), name="preview"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),
    path('search/', SearchList.as_view(), name="search"),
    path('author/page/<int:page>', SearchList.as_view(), name="search"),
]
