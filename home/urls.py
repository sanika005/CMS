from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    # user CURD API's
    path('user/create',create_user,name='create_user'),
    path('user/read/<int:pk>',read_user,name='read_user'),
    path('user/update/<int:pk>',update_user,name='update_user'),
    path('user/delete/<int:pk>',delete_user,name='delete_user'),

    # post CURD API's
    path('post/create',create_post,name='create_post'),
    path('post/read/<int:pk>',read_post,name='read_post'),
    path('post/update/<int:pk>',update_post,name='update_post'),
    path('post/delete/<int:pk>',delete_post,name='delete_post'),
    path('post/list',list_post,name='list_post'),

    # like CURD API's
    path('like/create',create_like,name='create_like'),
    path('like/read/<int:pk>',read_like,name='read_like'),
    path('like/update/<int:pk>',update_like,name='update_like'),
    path('like/delete/<int:pk>',delete_like,name='delete_like'),
]