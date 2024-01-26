# Generated by Django 4.2.7 on 2023-12-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_remove_approval_form_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model20fixedrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestername', models.CharField(max_length=100)),
                ('reason', models.TextField()),
                ('productname', models.CharField(max_length=100)),
                ('measurement', models.CharField(choices=[('GigaByte', 'GigaByte'), ('NumbersofItem', 'NumbersofItem'), ('Cartoon', 'Cartoon'), ('Meter', 'Meter'), ('inch', 'inch')], max_length=100)),
                ('NumberofItems', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Model20fixedrequest',
            },
        ),
    ]