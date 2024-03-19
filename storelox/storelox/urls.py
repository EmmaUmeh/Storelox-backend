"""
URL configuration for storelox project.

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
from ecommerce.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', home),
      path('my-view', my_view, name='my-view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint to obtain JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint to refresh JWT token
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login endpoint (using JWT)
    path('auth/register', Register_View, name='register'),  # Registration endpoint
    #    path('/my-view', my_view),
    # path('my-view', my_view, name='my-view'),
    # path('auth/login', TokenVerifyView(),  Login_View),
    #  path('auth/register', Register_View),
]
