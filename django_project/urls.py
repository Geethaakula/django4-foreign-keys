"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django_project.views import Home,UsersList,Gift,OtherUserGifts,Signup,Logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view()),
    path('register/',Signup.as_view()),
    path('users/',login_required(UsersList.as_view(), "/")),
    path('gifts/',login_required(Gift.as_view(), "/")),
    path('logout/',Logout.as_view()),
    path('othersgifts/<str:username>',OtherUserGifts.as_view())
]
