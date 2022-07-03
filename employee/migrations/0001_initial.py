# Generated by Django 3.2.13 on 2022-05-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('joiningdate', models.DateTimeField(auto_now=True)),
                ('dob', models.DateField()),
                ('phone', models.IntegerField()),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]