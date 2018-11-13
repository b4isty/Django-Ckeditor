from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_details/<int:pk>/$', views.blog_detail_view, name='blog_details'),
    path('blog_edit/<int:pk>/$', views.blog_edit_view, name='blog_edit'),
    path('blog_delete/<int:pk>/$', views.blog_delete, name='blog_delete')
]
