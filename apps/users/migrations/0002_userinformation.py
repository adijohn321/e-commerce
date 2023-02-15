# Generated by Django 4.0.1 on 2023-02-03 00:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('phone_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message="Mobile number format must be: '+639999999999'.", regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}')])),
                ('gender', models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')], max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_information', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]