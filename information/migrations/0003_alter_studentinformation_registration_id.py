# Generated by Django 4.0 on 2021-12-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_studentinformation_cr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='registration_ID',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]