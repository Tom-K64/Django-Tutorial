# Generated by Django 4.2.3 on 2023-07-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetailsmodel',
            name='standard',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodel',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
