# Generated by Django 4.1.7 on 2023-05-02 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symtoms', '0004_rename_uid_diseasesymtoms_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiseaseSymtoms',
            new_name='Questions',
        ),
    ]