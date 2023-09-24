from django.contrib import admin
from .models import FileModel, DocumentManagementModel

# Register your models here.
admin.site.register(FileModel)
admin.site.register(DocumentManagementModel)


