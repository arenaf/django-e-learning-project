# Generated by Django 5.1.4 on 2024-12-18 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Subject')),
                ('image', models.ImageField(blank=True, null=True, upload_to='subject', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('file', models.FileField(upload_to='file', verbose_name='File')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject', verbose_name='Subject')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
