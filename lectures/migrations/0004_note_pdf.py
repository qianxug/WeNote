# Generated by Django 4.1 on 2022-08-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='pdf',
            field=models.FileField(default='../media/', upload_to='uploads'),
        ),
    ]