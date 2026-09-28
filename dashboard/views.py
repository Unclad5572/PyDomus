from django.shortcuts import render
from account.decorators import mfa_required

@mfa_required
def home_view(request):
    return render(request, 'dashboard/index.html')

@mfa_required
def history_view(request):
    return render(request, 'dashboard/history.html')

@mfa_required
def alerts_view(request):
    return render(request, 'dashboard/alerts.html')

@mfa_required
def account_view(request):
    return render(request, 'dashboard/account.html')
