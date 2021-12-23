from django.conf import settings
from django.db import models


# Create your models here.
class StudentInformation(models.Model):
    registration_ID = models.CharField(max_length=10, primary_key=True)
    certificate_name = models.CharField(max_length=50, null=False)
    nickname = models.CharField(max_length=50)
    batch = models.IntegerField()
    phone_Number = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10, null=True)
    blood_Group = models.CharField(max_length=5, null=True)
    present_Address = models.CharField(max_length=170, null=True)
    permanent_Address = models.CharField(max_length=170, null=True)
    cr = models.CharField(max_length=6)


class ExtendedInformation(models.Model):
    registration_ID = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', default='pro.jpg')
    personal_email = models.EmailField(max_length=100)
    facebook = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)




