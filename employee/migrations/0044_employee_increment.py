# Generated by Django 3.2.13 on 2022-06-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0043_alter_employee_workeniversary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='increment',
            field=models.CharField(default='False', max_length=10),
        ),
    ]