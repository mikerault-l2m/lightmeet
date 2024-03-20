# Generated by Django 3.2.3 on 2024-03-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PsyMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=100)),
                ('entreprise', models.CharField(blank=True, max_length=100)),
                ('specialite', models.CharField(max_length=100)),
                ('anciennete', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='psy_images/')),
                ('site_web', models.URLField(blank=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Notre thérapeute professionnel',
                'verbose_name_plural': 'Nos thérapeutes professionnels',
            },
        ),
    ]
