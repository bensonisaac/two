# Generated by Django 4.2.5 on 2023-09-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
    ]