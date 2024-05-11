# Generated by Django 5.0.4 on 2024-05-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_alter_student_social_catagory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Social_catagory',
            field=models.CharField(choices=[('General', 'General'), ('OBC', 'Other Backward Class'), ('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe'), ('EWS', 'Economically Weaker Section')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='disablity',
            field=models.CharField(choices=[('None', 'None'), ('Visual', 'Visual Impairment'), ('Hearing', 'Hearing Impairment'), ('Mobility', 'Mobility Impairment'), ('Cognitive', 'Cognitive Impairment'), ('Other', 'Other')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('lkg', 'LKG'), ('ukg', 'UKG'), ('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('5', 'Grade 5'), ('6', 'Grade 6'), ('7', 'Grade 7'), ('8', 'Grade 8'), ('9', 'Grade 9'), ('10', 'Grade 10')], max_length=100),
        ),
    ]
