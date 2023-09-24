from pyexpat import model
from statistics import mode
from uuid import uuid4
from django.db import models
from .validator import validate_file_size
import uuid
import os
from authentication.models import User


def get_upload_path(instance , filename):
    return os.path.join(str(instance.folder.uid) , filename)

class UploadFile(models.Model):
    uid = models.UUIDField(primary_key= True , editable= False , default=uuid.uuid4)
    files = models.FileField(upload_to=get_upload_path, validators=[validate_file_size])
    created_at = models.DateField(auto_now= True)
    created_by = models.EmailField()


class FileModel(models.Model):
    upload_file = models.FileField(upload_to='file/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    shared_link = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.upload_file)



class DocumentManagementModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_documents')
    shared_link = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.title)
 



