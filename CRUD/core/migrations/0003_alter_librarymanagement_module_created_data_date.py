# Generated by Django 4.0.5 on 2022-09-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_librarymanagement_module_delete_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarymanagement_module',
            name='created_data_date',
            field=models.DateField(auto_now=True),
        ),
    ]