# Generated by Django 3.2.12 on 2023-11-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_Graph_Plotter', '0004_auto_20231110_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedcsv',
            name='y_label',
            field=models.CharField(default='Y', max_length=255),
        ),
    ]
