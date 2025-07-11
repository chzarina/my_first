from django.db import models

# Create your models here.

class Loyiha(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.ImageField(upload_to='loyiha', blank  = True, null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title