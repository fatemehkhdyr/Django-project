from django.urls import path
from django.contrib.auth import views
from .views import  ArticleList, Articlecreate, Articleupdate, ArticleDeleteView,Profile

app_name = "account"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('article/create', Articlecreate.as_view(), name="article-create"),
    path('article/update/<int:pk>', Articleupdate.as_view(), name="article-update"),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name="article-delete"),
    path('profile/', Profile.as_view(), name="profile"),
]
