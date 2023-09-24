from pyexpat import model
from rest_framework import serializers
from .models import *

class UploadFileSerializer(serializers.ModelSerializer):
  class Meta:
    model=FileModel
    fields = '__all__'



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentManagementModel
        fields = '__all__'
