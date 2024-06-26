# Generated by Django 5.0.4 on 2024-05-11 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Branch', '0003_remove_grades_branch_delete_branch_delete_grades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_code', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('pincode', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Branch.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Branch.branch')),
            ],
        ),
    ]
