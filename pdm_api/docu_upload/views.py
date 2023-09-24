from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class UploadFileView(GenericAPIView):
  serializer_class = UploadFileSerializer
  def post(self,  request, id, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'File Uploaded Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
  

            

class FileShareListView(GenericAPIView):
    def get(self, request, format=None):
        candidates = FileModel.objects.all()
        serializer = UploadFileSerializer(candidates, many=True)
        return Response({'status':'success', 'candidates':serializer.data }, status=status.HTTP_200_OK)



class DocumentManagementView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, document_id=None, shared_link=None):
        if shared_link:
            # Get the document using the shared link
            document = get_object_or_404(DocumentManagementModel, shared_link=shared_link)

            # Check if the requesting user is either the document owner or is in the document's shared_with list
            if request.user == document.owner or request.user in document.shared_with.all():
                serializer = DocumentSerializer(document)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("You are not allowed to view this document metadata.", status=status.HTTP_403_FORBIDDEN)

        elif document_id:
            # Get the document using the document_id parameter
            document = get_object_or_404(DocumentManagementModel, pk=document_id)

            # Check if the requesting user is either the document owner or is in the document's shared_with list
            if request.user == document.owner or request.user in document.shared_with.all():
                serializer = DocumentSerializer(document)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("You are not allowed to view this document met")

    def put(self, request, document_id):
        document = get_object_or_404(DocumentManagementModel, pk=document_id)

        # Check if the user is the owner of the document
        if request.user == document.owner:
            serializer = DocumentSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You are not allowed to update this document metadata.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, document_id):
        document = get_object_or_404(DocumentManagementModel, pk=document_id)

        # Check if the user is the owner of the document
        if request.user == document.owner:
            document.delete()
            return Response("Document deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("You are not allowed to delete this document.", status=status.HTTP_403_FORBIDDEN)

  
class GenerateSharedLink(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, document_id,shared_link):
        document = get_object_or_404(DocumentManagementModel, pk=document_id, shared_link=shared_link)

        # Check if the user is the owner of the document
        if request.user == document.owner:
            
            document.shared_link = uuid.uuid4()
            document.save()

           
            document.shared_with.add(request.user)

            # Get the current site's domain
            current_site = get_current_site(request)

            # Generate the full share link URL using the current site's domain and the shared_link attribute
            full_share_link = reverse('shared-link', kwargs={'shared_link': str(document.shared_link)})
            full_share_link = f"https://{current_site.domain}{full_share_link}"

            return Response({'shared_link': full_share_link}),
