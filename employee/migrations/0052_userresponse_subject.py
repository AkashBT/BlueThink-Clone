# Generated by Django 3.2.13 on 2022-06-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0051_alter_userresponse_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='subject',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
