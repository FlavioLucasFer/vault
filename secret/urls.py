from django.urls import path

from .views import FolderCreate, FolderDelete, FolderUpdate, SecretCreate, SecretDelete, SecretUpdate, TeamCreate, TeamDelete, TeamUpdate

urlpatterns = [
    path('create/team/', TeamCreate.as_view(), name='create-team'),
    path('create/folder/', FolderCreate.as_view(), name='create-folder'),
    path('create/secret/', SecretCreate.as_view(), name='create-secret'),

    path('edit/team/<int:pk>/', TeamUpdate.as_view(), name='edit-team'),
    path('edit/folder/<int:pk>/', FolderUpdate.as_view(), name='edit-folder'),
    path('edit/secret/<int:pk>/', SecretUpdate.as_view(), name='edit-secret'),
    
    path('delete/team/<int:pk>/', TeamDelete.as_view(), name='delete-team'),
    path('delete/folder/<int:pk>/', FolderDelete.as_view(), name='delete-folder'),
    path('delete/secret/<int:pk>/', SecretDelete.as_view(), name='delete-secret'),
]