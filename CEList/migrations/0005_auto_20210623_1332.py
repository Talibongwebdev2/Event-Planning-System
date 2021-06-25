# Generated by Django 3.1.6 on 2021-06-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CEList', '0004_auto_20210620_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_salary',
            old_name='Status',
            new_name='Total',
        ),
        migrations.AlterField(
            model_name='employee_info',
            name='Gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10),
        ),
    ]
