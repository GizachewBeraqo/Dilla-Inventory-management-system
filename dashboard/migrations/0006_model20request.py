# Generated by Django 4.2.7 on 2023-12-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_handover_higher_official1_approved_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model20request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('detailed_description', models.TextField()),
                ('measurement', models.CharField(max_length=100)),
                ('NumberofItems', models.IntegerField()),
                ('PriceofEach', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalcost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
