# Generated by Django 4.0 on 2021-12-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_alter_studentinformation_permanent_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='permanent_Address',
            field=models.CharField(max_length=170, null=True),
        ),
        migrations.AlterField(
            model_name='studentinformation',
            name='present_Address',
            field=models.CharField(max_length=170, null=True),
        ),
    ]
