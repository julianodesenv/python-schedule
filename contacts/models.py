from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):    
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    view = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='photos/%Y/%m')

    def __str__(self):
        return self.name
