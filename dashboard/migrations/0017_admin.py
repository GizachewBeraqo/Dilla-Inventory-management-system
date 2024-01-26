# Generated by Django 4.2.7 on 2023-12-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('experience', models.IntegerField(default=0)),
            ],
        ),
    ]
