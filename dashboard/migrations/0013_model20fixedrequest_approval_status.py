# Generated by Django 4.2.7 on 2023-12-12 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_delete_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='model20fixedrequest',
            name='approval_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50),
        ),
    ]
