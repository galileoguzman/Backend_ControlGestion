# Generated by Django 2.0.3 on 2018-04-10 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20180410_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='folio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.Document'),
        ),
    ]