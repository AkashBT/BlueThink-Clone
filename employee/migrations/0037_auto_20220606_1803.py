# Generated by Django 3.2.13 on 2022-06-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0036_alter_leavemanagement_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemanagement',
            name='rejectionreason',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='leavemanagement',
            name='reason',
            field=models.CharField(max_length=250),
        ),
    ]
