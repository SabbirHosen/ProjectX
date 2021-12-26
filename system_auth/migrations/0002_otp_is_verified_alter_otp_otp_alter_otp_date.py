# Generated by Django 4.0 on 2021-12-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='otp',
            name='OTP',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='otp',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]