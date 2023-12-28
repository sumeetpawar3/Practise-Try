from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=900)
    created_by = models.CharField(max_length=200)

