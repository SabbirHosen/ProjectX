# Generated by Django 3.2.6 on 2021-12-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationPrivacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_privacy', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=6)),
                ('email_privacy', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=6)),
                ('facebook_privacy', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=6)),
                ('github_privacy', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=6)),
                ('linkedin_privacy', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=6)),
                ('propic_privacy', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default='show', max_length=6)),
            ],
        ),
    ]
