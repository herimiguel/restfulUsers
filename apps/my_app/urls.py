from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^adding$', views.adding),
    url(r'^addUserPage$', views.addUserPage),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^(?P<id>\d+)/editUser$', views.editUser),
    url(r'^(?P<id>\d+)/showUser$', views.showUser),
    url(r'^(?P<id>\d+)/updateUser$', views.updateUser),
]
