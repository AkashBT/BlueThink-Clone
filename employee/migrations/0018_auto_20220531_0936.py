# Generated by Django 3.2.13 on 2022-05-31 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20220531_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='logindatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logindetails',
            name='logoutdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]