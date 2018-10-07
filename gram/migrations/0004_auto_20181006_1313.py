# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0003_auto_20181005_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_image', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=50, null=True)),
                ('image_caption', models.CharField(default='', max_length=50)),
                ('time_created', models.DateTimeField(auto_now=True)),
                ('time_updated', models.DateTimeField(auto_now_add=True)),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_bio', models.CharField(max_length=50)),
                ('profile_photo', models.ImageField(upload_to='profile/')),
            ],
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.Profile'),
        ),
    ]
