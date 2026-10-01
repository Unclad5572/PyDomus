from django.shortcuts import render
from account.decorators import mfa_required
from .models import SensorReading

# Alert thresholds (min, max) for numeric measurements
THRESHOLDS = {
    'temperature': (18, 24),
    'humidity': (30, 60),
}


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


def measurement(key):
    """Latest value of `key` with its thresholds and status: 'normal', 'low' or 'high'."""
    result = latest(key)
    if result is None:
        return None
    low, high = THRESHOLDS[key]
    result['min'], result['max'] = low, high
    if result['value'] < low:
        result['status'] = 'low'
    elif result['value'] > high:
        result['status'] = 'high'
    else:
        result['status'] = 'normal'
    return result

@mfa_required
def home_view(request):
    context = {
        'temperature': measurement('temperature'),
        'humidity': measurement('humidity'),
        'door': latest('contact'),
        'thresholds': THRESHOLDS,
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
