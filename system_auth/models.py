from django.db import models
from information.models import StudentInformation
# Create your models here.


class OTP(models.Model):
    registration_ID = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    auth_otp = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
