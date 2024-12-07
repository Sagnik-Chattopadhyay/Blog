from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000000000000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
