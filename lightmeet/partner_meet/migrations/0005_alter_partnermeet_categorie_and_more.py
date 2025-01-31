# Generated by Django 4.2.3 on 2025-01-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_meet', '0004_rename_visites_france_partnermeet_visites_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnermeet',
            name='categorie',
            field=models.CharField(choices=[('Généraliste', 'Site généraliste'), ('Senior', 'Site senior'), ('Haut-de-gamme', 'Site haut-de-gamme')], default='Généraliste', max_length=25),
        ),
        migrations.AlterField(
            model_name='partnermeet',
            name='relation',
            field=models.CharField(choices=[('Durables', 'Durables'), ('LGBTQ+', 'LGBTQ+')], default='Toutes', max_length=25),
        ),
    ]
