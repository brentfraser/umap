# Generated by Django 2.0.7 on 2018-07-14 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umap', '0004_add_licence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='tilelayer',
        ),
    ]