"""
URL configuration for django_simple project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import home_process_function
from about.views import about
from contacts.views import contacts
from post.views import post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_process_function, name='home_url_name'),
    path('about/', about, name='about_url_name'),
    path('contacts/', contacts, name='contacts_url_name'),
    path('post/', post, name='post_url_name')
]
