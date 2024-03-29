# Generated by Django 5.0.1 on 2024-02-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='events')),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
    ]
