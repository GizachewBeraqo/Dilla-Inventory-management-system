# Generated by Django 4.2.7 on 2023-12-13 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_admin_handover_current_admin_handover_is_approved'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]