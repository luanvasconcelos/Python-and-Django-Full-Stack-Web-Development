from django.conf.urls import url
from app2 import views

urlpatterns =[
    url('', views.users, name='users'),
]
