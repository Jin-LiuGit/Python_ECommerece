# Generated by Django 2.2.6 on 2020-03-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_partnercustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='url_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partner',
            name='url_short',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
