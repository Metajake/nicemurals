from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about', views.about, name="about"),
    re_path(r'^tags/(?P<blog_tagslug>[\w-]+)', views.taglist, name="tag-list"), #starts with tags/ followed by a tagslug followed by one or more groups of any letters or numbers ending with -
    re_path(r'^projects/(?P<category_slug>[\w-]+)', views.categorylist, name="category-list"),
    re_path(r'^entry/(?P<entry_slug>[\w-]+)', views.entry, name="entry"),
    re_path(r'^project/(?P<project_slug>[\w-]+)', views.project, name="project"),
    re_path(r'^ajax/tweet-entry/', views.tweetEntry, name="tweet-entry"),
]
