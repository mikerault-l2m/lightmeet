# Generated by Django 4.2.3 on 2024-09-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supportticket',
            options={'verbose_name': 'Contact avec le client', 'verbose_name_plural': 'Contacts avec les clients'},
        ),
        migrations.AlterField(
            model_name='supportticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='supportticket',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='supportticket',
            name='sender_email',
            field=models.EmailField(max_length=254, verbose_name="Adresse e-mail de l'expéditeur"),
        ),
        migrations.AlterField(
            model_name='supportticket',
            name='subject',
            field=models.CharField(choices=[('Informations', 'Je souhaite en savoir plus'), ('Partenariat', 'Je cherche à réaliser un partenariat'), ('Technique', 'Soucis technique sur la plateforme')], default='', max_length=25, verbose_name='Sujet'),
        ),
    ]
