# Generated by Django 3.2.13 on 2022-05-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_alter_logindetails_logoutdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='logoutdatetime',
            field=models.DateTimeField(default=''),
        ),
    ]
