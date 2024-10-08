# Generated by Django 4.2.3 on 2024-09-27 11:17

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
                ('LOGO', models.ImageField(blank=True, null=True, upload_to='MeetSites/')),
                ('url', models.URLField(blank=True)),
                ('Visites_France', models.CharField(max_length=100)),
                ('categorie', models.CharField(choices=[('Généraliste', 'Site généraliste'), ('Libertin', 'Site libertin'), ('Senior', 'Site senior'), ('Religieux', 'Site religieux'), ('Haut-de-gamme', 'Site haut-de-gamme'), ('Généraliste', 'Site généraliste'), ('Senior', 'Site senior'), ('Haut-de-gamme', 'Site haut-de-gamme')], default='Généraliste', max_length=25)),
                ('relation', models.CharField(choices=[('Durables', 'Durables'), ("Relation d'un soir", "Relation d'un soir"), ('Homosexuelles', 'Homosexuelles'), ('Durables', 'Durables'), ('Homosexuelles', 'Homosexuelles')], default='Toutes', max_length=25)),
                ('age', models.CharField(choices=[('18-30', '18-30 '), ('31-45', '31-45 '), ('+ 46', '+ 46')], max_length=50)),
                ('prix_avg', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('trustpilot', models.FloatField(blank=True, null=True)),
                ('affiliation', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=False)),
                ('co2', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('ranking', models.PositiveIntegerField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Notre site de rencontre partenaire',
                'verbose_name_plural': 'Nos sites de rencontres partenaires',
            },
        ),
    ]
