# Generated by Django 4.2.3 on 2023-07-22 16:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docu_upload', '0005_documentmanagement_shared_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DocumentManagement',
            new_name='DocumentManagementModel',
        ),
    ]
