from django.urls import path
from .views import UploadFileView, GenerateSharedLink, DocumentManagementView, FileShareListView


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('upload', UploadFileView.as_view()),
    path('files', FileShareListView.as_view()),
    path('documents/<int:document_id>/', DocumentManagementView.as_view(), name='document-metadata'),
    path('documents/<int:document_id>/<str:shared_link>/', DocumentManagementView.as_view(), name='shared-link'),
    path('documents/<int:document_id>/generate-link/', GenerateSharedLink.as_view(), name='generate-shared-link'),
]