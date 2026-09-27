from django.shortcuts import render, redirect

def home_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return render(request, 'dashboard/index.html')
    else:
        return redirect('login')

def history_view(request):
    return render(request, 'dashboard/history.html')

def alerts_view(request):
    return render(request, 'dashboard/alerts.html')

def account_view(request):
    return render(request, 'dashboard/account.html')