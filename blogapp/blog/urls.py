from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.index, name='index'),
    path('makepost/', views.make_post, name='makepost'),
    path('post_datails/<int:pk>/', views.post_details, name='post_details'),
    path('edit_post/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
      path('toggle_repost/<int:post_id>/', views.toggle_repost, name='toggle_repost'),

]