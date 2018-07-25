from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^blog_list/', views.blog_list, name='blog_list'),
    url(r'^blog_details/(?P<pk>\d+)/$', views.blog_detail_view, name='blog_details'),
    url(r'^blog_edit/(?P<pk>\d+)/$', views.blog_edit_view, name='blog_edit'),
    url(r'^blog_delete/(?P<pk>\d+)/$', views.blog_delete, name='blog_delete')
]
