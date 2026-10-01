from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def mfa_required(view):
    """Allow access only to logged-in users who have validated their TOTP code."""
    @wraps(view)
    @login_required
    def wrapper(request, *args, **kwargs):
        if not request.session.get('mfa_verified', False):
            return redirect('login-mfa')
        return view(request, *args, **kwargs)
    return wrapper
