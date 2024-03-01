from django.urls import path
from . import views

urlpatterns=[
  path(  '',views.blog_index, name='blog_index'),
  path('post/<int:pk>/',views.blog_detail,name='blog_detail'),
  path('catagory/<c>',views.blog_catagory,name='blog_catagory')
]