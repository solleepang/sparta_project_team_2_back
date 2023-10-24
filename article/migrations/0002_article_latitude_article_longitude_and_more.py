# Generated by Django 4.2.6 on 2023-10-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=11, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='store_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]