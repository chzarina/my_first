# Generated by Django 5.2.3 on 2025-06-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yangilik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=200)),
                ('matn', models.TextField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('muallif', models.CharField(default='Admin', max_length=100)),
            ],
        ),
    ]
