# Generated by Django 3.1.6 on 2021-06-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEList', '0003_remove_employee_info_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_info',
            name='Address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Company_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Contact_No',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Emailaddress',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]
