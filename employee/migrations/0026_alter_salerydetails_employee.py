# Generated by Django 3.2.13 on 2022-06-02 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0025_rename_total_salerydetails_totalsalary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salerydetails',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', unique=True),
        ),
    ]
