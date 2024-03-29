# Generated by Django 4.2.7 on 2023-12-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_model20request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propertyreturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('measurement', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('Condition_of_property_recently', models.CharField(choices=[('working', 'Working'), ('Notworking', 'NotWorking ')], max_length=100)),
                ('PriceofEach', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalcost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Propertyreturn',
            },
        ),
        migrations.AlterModelOptions(
            name='model20request',
            options={'verbose_name_plural': 'Model20request'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
    ]
