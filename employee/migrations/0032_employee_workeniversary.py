# Generated by Django 3.2.13 on 2022-06-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0031_auto_20220606_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='workeniversary',
            field=models.IntegerField(default=1),
        ),
    ]
