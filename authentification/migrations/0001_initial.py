# Generated by Django 5.1.4 on 2024-12-09 16:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=150, null=True)),
                ('prenom', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
