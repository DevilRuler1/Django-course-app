# Generated by Django 3.1.3 on 2023-04-14 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='content',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='lesson',
            new_name='lesson_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_text',
        ),
    ]
