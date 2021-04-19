"""FPSysApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from fpsystem import views
from django.contrib import admin
from django.urls import path
urlpatterns = [ 
    #url(r'^$', include('fpsystem.urls')), 
   # url(r'^fpsystem/roomno/(?P<roomno>[0-9]+)/$', views.Attendance),
    #url(r'^fpsystem/$', views.Login),
    #url('hello/', views.hello),
    #url(r'^fpsystem/room/(?P<room_no>\d+)$', views.Attendance),
    #url(r'^fpsystem/room/$', views.Attendance),
    #url(r'^fpsystem/login/(?P<employeeID>\d+)/(?P<password>\d+)$', views.Login),
    #url(r'^search-post/$', views.Attendance),
    #path('admin/', admin.site.urls),
    #path('hello/',views.post),
    #url('fpsystem/room', views.Attendance),
    path('fpsystem/room', views.Attendance),
    path('fpsystem/login', views.Login),

]
