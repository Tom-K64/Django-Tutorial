# Generated by Django 4.2.3 on 2023-07-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basics', '0004_alter_studentmodel_contact_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
