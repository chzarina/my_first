# Generated by Django 5.2.3 on 2025-06-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loyiha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('images', models.ImageField(blank=True, null=True, upload_to='loyiha')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
