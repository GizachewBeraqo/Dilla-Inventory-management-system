from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, null=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images')


    def __str__(self):
        return self.user.username

   # def __str__(self):
      #  return f'{self.user.username}-Profile'

    class Meta:
        verbose_name_plural = 'profiles'
    
    
      
