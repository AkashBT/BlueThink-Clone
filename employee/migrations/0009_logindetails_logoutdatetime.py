# Generated by Django 3.2.13 on 2022-05-13 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20220513_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='logoutdatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
