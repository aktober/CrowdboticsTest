"""CrowdboticsTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from app import views
from django.contrib.auth.decorators import login_required
from app.api import views as api_views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^login/$', views.LoginPage.as_view(), name='login'),
    url(r'^register/$', views.RegisterPage.as_view(), name='register'),
    url(r'^admin/', admin.site.urls),

    url(r'^api/dogs/$', login_required(api_views.DogList.as_view()),
        name='api-dogs-list'),
    url(r'^api/dogs/(?P<pk>[-\w]+)/$', login_required(api_views.DogDetail.as_view()),
        name='api-dog'),

    url(r'^api/cats/$', login_required(api_views.CatList.as_view()),
        name='api-cats-list'),
    url(r'^api/cats/(?P<pk>[-\w]+)/$', login_required(api_views.CatDetail.as_view()),
        name='api-cat'),
]
