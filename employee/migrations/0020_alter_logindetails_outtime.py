# Generated by Django 3.2.13 on 2022-06-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_auto_20220531_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='outtime',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
