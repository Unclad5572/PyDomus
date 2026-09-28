"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path,include
from account.views import login_view, register_view, mfa_view
from dashboard.views import home_view, alerts_view, history_view, account_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('login-mfa/', mfa_view, name='login-mfa'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('history/', history_view, name='history'),
    path('alerts/', alerts_view, name='alerts'),
    path('account/', account_view, name='account'),
]
