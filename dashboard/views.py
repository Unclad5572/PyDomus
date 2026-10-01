from django.shortcuts import render
from account.decorators import mfa_required
from .models import SensorReading


def latest(key):
    """Most recent value of `key` sent by any sensor, or None if never received."""
    reading = SensorReading.objects.filter(data__has_key=key).first()
    if reading is None:
        return None
    return {
        'value': reading.data[key],
        'topic': reading.topic,
        'received_at': reading.received_at,
    }

@mfa_required
def home_view(request):
    context = {
        'temperature': latest('temperature'),
        'humidity': latest('humidity'),
        'door': latest('contact'),
    }
    return render(request, 'dashboard/index.html', context)

@mfa_required
def history_view(request):
    return render(request, 'dashboard/history.html')

@mfa_required
def alerts_view(request):
    return render(request, 'dashboard/alerts.html')

@mfa_required
def account_view(request):
    return render(request, 'dashboard/account.html')
