# Generated by Django 4.2.1 on 2023-05-24 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question_txt',
        ),
    ]
