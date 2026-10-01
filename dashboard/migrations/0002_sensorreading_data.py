import json

from django.db import migrations, models


def value_to_data(apps, schema_editor):
    SensorReading = apps.get_model('dashboard', 'SensorReading')
    # Zigbee2MQTT internal messages are no longer stored
    SensorReading.objects.filter(topic__contains='/bridge/').delete()
    for reading in SensorReading.objects.all():
        try:
            data = json.loads(reading.value)
        except json.JSONDecodeError:
            data = None
        reading.data = data if isinstance(data, dict) else {'value': reading.value}
        reading.save(update_fields=['data'])


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorreading',
            name='data',
            field=models.JSONField(default=dict),
        ),
        migrations.RunPython(value_to_data, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='sensorreading',
            name='value',
        ),
    ]
