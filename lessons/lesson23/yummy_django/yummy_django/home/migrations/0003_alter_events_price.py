# Generated by Django 5.0.1 on 2024-02-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
