# Generated by Django 3.2.9 on 2021-11-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piec_CO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature_in',
            name='date',
            field=models.TimeField(auto_now_add=True),
        ),
    ]