# Generated by Django 5.0.1 on 2024-03-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catagory',
            options={'verbose_name_plural': 'catagories'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='createn_on',
            new_name='created_on',
        ),
    ]