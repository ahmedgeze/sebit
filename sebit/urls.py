"""sebit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views as d



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # path('/',include('sebit_json_api.urls'),name='index'),
    url(r'^get/$', d.home, name='homepage'),
    url(r'^post/(?P<name>\w{0,50})/(?P<city>\w{0,50})/(?P<country>\w{0,50})$',d.post,name='post'),
    url(r'^put/$',d.put,name='putdata'),
    # url(r'^get/$',d.get,name='top25'),

]
