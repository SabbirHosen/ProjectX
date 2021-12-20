from django.db import models


# Create your models here.
class InformationPrivacy(models.Model):
    choiceStatus = [
        ('show', 'show'),
        ('hide', 'hide'),
    ]
    present_address = models.CharField(choices=choiceStatus, default='hide', max_length=6)
    permanent_address = models.CharField(choices=choiceStatus, default='hide', max_length=6)
    phone_privacy = models.CharField(choices=choiceStatus, default='hide', max_length=6)
    email_privacy = models.CharField(choices=choiceStatus, default='show', max_length=6)
    facebook_privacy = models.CharField(choices=choiceStatus, default='show', max_length=6)
    github_privacy = models.CharField(choices=choiceStatus, default='show', max_length=6)
    linkedin_privacy = models.CharField(choices=choiceStatus, default='show', max_length=6)
    propic_privacy = models.CharField(choices=choiceStatus, default='show', max_length=6)
