# Generated by Django 5.0.4 on 2024-05-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_myuser_is_staffadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sats_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
