from django.conf.urls import url
from scrapper import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    ]

