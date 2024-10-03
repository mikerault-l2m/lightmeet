# Generated by Django 4.2.3 on 2024-09-27 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_visitor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lightener',
            options={'verbose_name': 'Compte utilisateur', 'verbose_name_plural': 'Comptes utilisateurs'},
        ),
        migrations.AlterModelOptions(
            name='visitor',
            options={'verbose_name': 'Visiteur de Lightmeet', 'verbose_name_plural': 'Visiteurs de Lightmeet'},
        ),
        migrations.AlterField(
            model_name='lightener',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='clic_comparer',
            field=models.PositiveIntegerField(default=0, verbose_name='Clics Comparer'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='clic_rencontres',
            field=models.PositiveIntegerField(default=0, verbose_name='Clics Rencontres'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='clic_therapeutes',
            field=models.PositiveIntegerField(default=0, verbose_name='Clics Thérapeutes'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='consentement',
            field=models.BooleanField(default=False, verbose_name='Consentement'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='engagement',
            field=models.PositiveIntegerField(default=0, verbose_name='Engagement'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='favorite_app',
            field=models.PositiveIntegerField(default=0, verbose_name='Application préférée'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='Adresse IP'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Actif'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Administrateur'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Membre du personnel'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='last_weekly_reset',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Dernière réinitialisation hebdomadaire'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Localisation'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='prenom',
            field=models.CharField(blank=True, max_length=25, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='weekly_favorites',
            field=models.PositiveIntegerField(default=0, verbose_name='Favoris hebdomadaires'),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='weekly_likes',
            field=models.PositiveIntegerField(default=0, verbose_name="J'aime hebdomadaires"),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='Adresse IP'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Localisation'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Horodatage'),
        ),
    ]