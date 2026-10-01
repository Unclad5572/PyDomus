from django.contrib import admin
from .models import SensorReading


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = ('topic', 'value', 'received_at')
    list_filter = ('topic',)

