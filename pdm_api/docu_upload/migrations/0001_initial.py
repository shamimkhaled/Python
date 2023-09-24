# Generated by Django 4.2.3 on 2023-07-22 14:35

from django.db import migrations, models
import docu_upload.models
import docu_upload.validator
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('files', models.FileField(upload_to=docu_upload.models.get_upload_path, validators=[docu_upload.validator.validate_file_size])),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
            ],
        ),
    ]
