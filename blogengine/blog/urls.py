from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list_url'),
    path('post', PostList.as_view(), name='post_list_url'),
    path('post_create', PostCreate.as_view(), name='post_create_url'),
    path('post=<str:instance_id>', PostDetail.as_view(), name='post_detail_url'),
    path('post_update=<str:instance_id>', PostUpdate.as_view(), name='post_update_url'),
    path('post_delete=<str:instance_id>', PostDelete.as_view(), name='post_delete_url'),
    path('tag', TagsList.as_view(), name='tag_list_url'),
    path('tag_create', TagCreate.as_view(), name='tag_create_url'),
    path('tag=<str:instance_id>', TagDetail.as_view(), name='tag_detail_url'),
    path('tag_update=<str:instance_id>', TagUpdate.as_view(), name='tag_update_url'),
    path('tag_delete=<str:instance_id>', TagDelete.as_view(), name='tag_delete_url'),
]
