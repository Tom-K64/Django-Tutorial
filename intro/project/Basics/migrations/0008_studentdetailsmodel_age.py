# Generated by Django 4.2.3 on 2023-08-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basics', '0007_subjectmodel_alter_studentmodel_organisation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetailsmodel',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
