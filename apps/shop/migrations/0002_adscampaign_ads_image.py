# Generated by Django 4.0.1 on 2023-02-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adscampaign',
            name='ads_image',
            field=models.ImageField(default='ad1.jfif', upload_to='Ads_Images'),
        ),
    ]
