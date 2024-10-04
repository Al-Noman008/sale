from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_num = models.CharField(max_length=15)
    address = models.TextField(max_length=30)
    wesite = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=30 , blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    

class UserOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}' OTP"

            
