# Generated by Django 3.2.13 on 2022-05-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('loginfrom', models.CharField(max_length=50)),
            ],
        ),
    ]
