from django.db import models
from users.models import User
# Create your models here.

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title or "No Title"

    class Meta:
        verbose_name_plural = 'Images'