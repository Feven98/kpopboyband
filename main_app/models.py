from django.db import models

# Create your models here.
class BoyBand(models.Model):

    group_name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    member = models.TextField(max_length=100)
    bio = models.TextField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ['group_name']