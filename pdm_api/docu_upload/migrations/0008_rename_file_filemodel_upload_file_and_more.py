# Generated by Django 4.2.3 on 2023-07-22 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docu_upload', '0007_documentmanagementmodel_shared_with'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='file',
            new_name='upload_file',
        ),
        migrations.RemoveField(
            model_name='filemodel',
            name='date',
        ),
        migrations.AddField(
            model_name='filemodel',
            name='uploaded_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
