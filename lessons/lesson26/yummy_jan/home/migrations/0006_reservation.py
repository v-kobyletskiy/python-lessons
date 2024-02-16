# Generated by Django 5.0.2 on 2024-02-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('number_people', models.PositiveSmallIntegerField()),
                ('is_conformed', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]