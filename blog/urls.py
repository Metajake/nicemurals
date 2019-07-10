from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    re_path(r'^tags/(?P<blog_tagslug>[\w-]+)', views.taglist, name="tag-list"), #starts with tags/ followed by a tagslug followed by one or more groups of any letters or numbers ending with -
    re_path(r'^entry/(?P<entry_slug>[\w-]+)', views.entry, name="entry"), 
]
