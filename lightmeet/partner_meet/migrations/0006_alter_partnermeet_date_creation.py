# Generated by Django 4.2.3 on 2024-05-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner_meet', '0005_alter_partnermeet_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnermeet',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]