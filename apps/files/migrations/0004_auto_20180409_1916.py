# Generated by Django 2.0.3 on 2018-04-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_remove_document_fechaexp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='annexes',
            field=models.FileField(blank=True, null=True, upload_to='archivosenviados/'),
        ),
    ]
