# Generated by Django 3.1.6 on 2021-06-25 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CEList', '0009_remove_branch_company_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_report',
            name='Company_rating',
        ),
    ]
