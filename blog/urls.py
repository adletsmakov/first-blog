from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^post', views.post_list, name='post_list'),
     url(r'^form', views.form, name='form'),
     url(r'^why', views.why, name='why'),
     url(r'^maps', views.maps, name='maps'),
     url(r'^news', views.news, name='news'),
    
]
