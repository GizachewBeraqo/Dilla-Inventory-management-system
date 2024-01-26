# Generated by Django 4.2.7 on 2023-12-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_remove_model20fixedrequest_approval_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='form',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('fixed', 'fixed'), ('non-fixed', 'non-fixed')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Model20fixedrequest',
        ),
    ]