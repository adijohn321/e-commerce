# Generated by Django 4.0.1 on 2023-02-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
