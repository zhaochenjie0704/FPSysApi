from django.conf.urls import url 
from fpsystem import views 
from django.contrib import admin
from django.urls import path
 
urlpatterns = [ 
    #url(r'^fpsystem/roomno/(?P<roomno>[0-9]+)/$', views.Attendance),
    #url(r'^fpsystem/$', views.Login),
    #url('hello/', views.hello),
    #url('fpsystem/', views.Attendance),
    #url(r'^search-post/$', views.Attendance),
    #path('hello/',views.post),
    #url(r'^postTest1/$', views.postTest1),
    #url('fpsystem/room', views.Attendance),
    path('fpsystem/room/', views.Attendance),
    url('fpsystem/login', views.Login),
]
