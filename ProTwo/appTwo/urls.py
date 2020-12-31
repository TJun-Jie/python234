from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url('users', views.users, name='users'),
    url('forms', views.form_name_view, name='form')
]