# Generated by Django 5.1.4 on 2024-12-18 15:58

import django.db.models.deletion
import registration.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=registration.models.custom_avatar, verbose_name='Avatar')),
                ('is_teacher', models.BooleanField(default=True)),
                ('students', models.ManyToManyField(blank=True, to='registration.profile')),
                ('subjects', models.ManyToManyField(blank=True, related_name='subject', to='subject.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]