# Generated by Django 3.2.13 on 2022-05-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_alter_logindetails_logoutdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='logoutdatetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]