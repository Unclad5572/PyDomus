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
