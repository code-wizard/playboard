# Generated by Django 2.1.7 on 2019-04-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_pbconfig_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbavailableplaforms',
            name='installation_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]