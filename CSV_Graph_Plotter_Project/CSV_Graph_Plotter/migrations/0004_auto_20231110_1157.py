# Generated by Django 3.2.12 on 2023-11-10 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_Graph_Plotter', '0003_auto_20231108_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedcsv',
            old_name='x1_column',
            new_name='y1_column',
        ),
        migrations.RenameField(
            model_name='uploadedcsv',
            old_name='x2_column',
            new_name='y2_column',
        ),
        migrations.RenameField(
            model_name='uploadedcsv',
            old_name='x3_column',
            new_name='y3_column',
        ),
    ]
