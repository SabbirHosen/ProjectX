# Generated by Django 4.0 on 2021-12-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinformation',
            name='cr',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
