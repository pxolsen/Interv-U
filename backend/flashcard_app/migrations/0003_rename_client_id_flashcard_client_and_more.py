# Generated by Django 4.2.6 on 2023-10-14 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard_app', '0002_rename_question_flashcard_question_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashcard',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='flashcard',
            old_name='question_id',
            new_name='question',
        ),
    ]