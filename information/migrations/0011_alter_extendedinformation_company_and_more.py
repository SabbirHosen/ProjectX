# Generated by Django 4.0 on 2021-12-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0010_alter_extendedinformation_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedinformation',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extendedinformation',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extendedinformation',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extendedinformation',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extendedinformation',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extendedinformation',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
