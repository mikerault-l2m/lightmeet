# Generated by Django 4.2.3 on 2024-04-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='MeetSites/')),
                ('genre_find', models.CharField(choices=[('Homme', 'Je cherche un homme'), ('Femme', 'Je cherche une femme'), ('Non déterminé', 'Je cherche tout le monde')], default='Non déterminé', max_length=25)),
                ('relation', models.CharField(choices=[('durables', 'Durables'), ("Relation d'un soir", "Relation d' un soir"), ('toutes', 'Toutes')], max_length=50)),
                ('age', models.CharField(choices=[('18-25', '18-25 ans'), ('25-35', '25-35 ans'), ('35-45', '35-45 ans'), ('45-55', '45-55 ans'), ('plus', 'Plus de 55 ans')], max_length=50)),
                ('prix_avg', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('innovation', models.TextField(blank=True, null=True)),
                ('ranking', models.PositiveIntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True)),
                ('affiliation', models.BooleanField(default=False)),
                ('categorie', models.CharField(max_length=100)),
                ('nombre_visiteurs_par_mois', models.PositiveIntegerField()),
                ('pourcentage_femmes', models.FloatField(blank=True, null=True)),
                ('tranche_age', models.CharField(max_length=50)),
                ('google_trustpilot_avg', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('storytelling_comment', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Notre site de rencontre partenaire',
                'verbose_name_plural': 'Nos sites de rencontres partenaires',
            },
        ),
    ]
