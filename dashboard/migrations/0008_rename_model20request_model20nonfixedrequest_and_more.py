# Generated by Django 4.2.7 on 2023-12-11 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_propertyreturn_alter_model20request_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model20request',
            new_name='Model20Nonfixedrequest',
        ),
        migrations.AlterModelOptions(
            name='model20nonfixedrequest',
            options={'verbose_name_plural': 'Model20Nonfixedrequest'},
        ),
    ]