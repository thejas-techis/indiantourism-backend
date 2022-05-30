# Generated by Django 4.0.3 on 2022-05-21 13:40

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wonder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('description', models.CharField(db_index=True, max_length=5000, verbose_name='Description')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
                ('time_to_travel1', models.CharField(max_length=100, verbose_name='Time To Travel1')),
                ('time_to_travel2', models.CharField(max_length=100, verbose_name='Time To Travel2')),
                ('time_to_travel3', models.CharField(max_length=100, verbose_name='Time To Travel3')),
                ('googel_map_link', models.CharField(max_length=500, verbose_name='Googel Map Link')),
                ('google_map_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Google Map Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated_at')),
            ],
            options={
                'db_table': 'wonder',
            },
        ),
    ]
