from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm, MfaForm
from django_totp.auth import is_totp_enabled
from django_totp.totp import verify_totp_code, create_totp_setup, confirm_totp_setup
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import base64

def home_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return render(request, 'index.html')
    else:
        return redirect('login')

@login_required
def mfa_view(request):
    user = request.user
    mfa_enabled = is_totp_enabled(user)
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return redirect('/')
    request.session['mfa_verified'] = False # Set the MFA verification status to False at the start of the view
    qr_base64 = None  # Initialize qr_base64 to None if MFA is enabled
    if request.method == 'POST':
        form = MfaForm(request.POST)
        action = request.POST.get('action')

        if form.is_valid():
            totp_code = form.cleaned_data['totp_code']
            if action == 'verify-totp':
                if verify_totp_code(user, totp_code): 
                    request.session['mfa_verified'] = True
                    return redirect('/')
                form.add_error('totp_code', 'Code TOTP invalide')

            elif action == 'confirm-setup':
                try:
                    confirm_totp_setup(user, totp_code)
                    request.session['mfa_verified'] = True
                    request.session.pop('pending_qr', None) # Remove the pending QR code from the session after successful setup
                    return redirect('/')
                except Exception: # if the TOTP code is invalid, an exception will be raised
                    form.add_error('totp_code', 'Code TOTP invalide')
        mfa_enabled = is_totp_enabled(user)

    else:
        form = MfaForm()
    
    if not mfa_enabled:
        # If MFA is not enabled, generate a new QR code and store it in the session if it doesn't already exist
        if 'pending_qr' in request.session:
            qr_base64 = request.session['pending_qr']
        else:
            svg_qr_code = create_totp_setup(user)
            qr_base64 = base64.b64encode(svg_qr_code.encode('utf-8')).decode('ascii')
            request.session['pending_qr'] = qr_base64
    
    return render(request, 'login_mfa.html', {'form': form, 'qr':qr_base64, 'mfa_enabled': mfa_enabled})



def account_view(request):
    if request.session.get('mfa_verified', False): # If the user has already verified MFA, redirect them to the home page
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('login-mfa')  # Redirect to the MFA page after successful login
            form.add_error(None, 'Adresse e-mail ou mot de passe invalide')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})
    
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            form.save() # Save the new user to the database
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={'form': form})