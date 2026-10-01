from django.db import models


class SensorReading(models.Model):
    topic = models.CharField(max_length=255, db_index=True)
    data = models.JSONField(default=dict)
    received_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-received_at']

    def __str__(self):
        return f"[{self.topic}] {self.data} ({self.received_at:%Y-%m-%d %H:%M:%S})"
