from django.shortcuts import render, redirect

def home_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return render(request, 'dashboard/index.html')
    else:
        return redirect('login')

def history_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return render(request, 'dashboard/history.html')
    else:
        return redirect('login')
    
def alerts_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return render(request, 'dashboard/alerts.html')
    else:
        return redirect('login')

def account_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return render(request, 'dashboard/account.html')
    else:
        return redirect('login')