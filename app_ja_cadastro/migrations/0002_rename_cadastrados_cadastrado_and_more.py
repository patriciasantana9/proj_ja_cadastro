# Generated by Django 4.2.5 on 2023-10-04 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ja_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cadastrados',
            new_name='Cadastrado',
        ),
        migrations.RenameField(
            model_name='cadastrado',
            old_name='id_cadastrados',
            new_name='id_cadastrado',
        ),
    ]