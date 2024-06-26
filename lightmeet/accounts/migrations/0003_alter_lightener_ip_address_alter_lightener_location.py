# Generated by Django 4.2.3 on 2024-05-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_lightener_ip_address_alter_lightener_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightener',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lightener',
            name='location',
            field=models.CharField(blank=True, default=False, max_length=100),
        ),
    ]
