from django.conf import settings
from django.db import models
from information.models import StudentInformation


# Create your models here.
class BloodInformation(models.Model):
    registration_ID = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    last_donated = models.DateField(['%m/%d/%y'], blank=True)
    want_donate = models.CharField(max_length=10)
