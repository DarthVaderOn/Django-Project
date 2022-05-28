from django.db import models

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=128, null=False, blank=False, unique=True)