# Generated by Django 5.0.2 on 2024-02-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery')),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(default=1)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]