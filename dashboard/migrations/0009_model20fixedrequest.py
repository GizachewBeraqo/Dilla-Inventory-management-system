# Generated by Django 4.2.7 on 2023-12-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_rename_model20request_model20nonfixedrequest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model20fixedrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('detailed_description', models.TextField()),
                ('measurement', models.CharField(max_length=100)),
                ('NumberofItems', models.IntegerField()),
                ('PriceofEach', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalcost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Model20fixedrequest',
            },
        ),
    ]
