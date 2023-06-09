"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from example.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', example,name='example_home'),
    path('login/', login,name='login'),
    path('login_auth/', login_auth,name='login_auth'),
    path('contact/', contact,name='contact'),
    path('post_query/', post_query,name='post_query'),
    path('adminHome/', adminHome,name='adminHome'),
    path('get_user_query/', get_user_query,name='get_user_query'),
    path('', contact,name='contact'),
]
