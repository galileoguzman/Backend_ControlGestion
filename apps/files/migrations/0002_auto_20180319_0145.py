# Generated by Django 2.0.3 on 2018-03-19 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importan',
            old_name='namepri',
            new_name='nameimp',
        ),
    ]
