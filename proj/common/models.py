from django.db import models

# Create your models here.

class Request(models.Model):
    phone = models.CharField(max_length=12, null=False, blank=False)
    connection_type = models.CharField(max_length=12)
    name = models.CharField(max_length=150, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
