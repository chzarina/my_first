from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    images = models.ImageField(upload_to='group', blank  = True, null=True)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
