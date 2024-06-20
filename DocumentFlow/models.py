from django.db import models
from django.contrib.auth.models import User
import os

class Employee(models.Model):
    
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


STATUS_PENDING = 'PENDING'
STATUS_COMPLETE = 'COMPLETE'
STATUS_FAILED = 'FAILED'

STATUS_CHOICES = [
    (STATUS_PENDING , 'PENDING'),
    (STATUS_COMPLETE , 'COMPLETE'),
    (STATUS_FAILED , 'FAILED'),

]


class File(models.Model):
    FILE_TYPE_CHOICES = [
        ('.txt', '.txt'),
        ('.csv', '.csv'),
        ('.json', '.json'),
        ('.docx', '.docx'),
        ('.pdf', '.pdf'),
        ('.jpg', '.jpg'),
        ('.mp3', '.mp3'),
        ('.mp4', '.mp4'),
    ]

    file = models.FileField(upload_to='static/uploads/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_files', null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    rejection_notes = models.TextField(blank=True)
    
    
    def __str__(self):
        return os.path.basename(self.file.name)
    

class FileRequest(models.Model):
    REQUESTED = 'Requested'
    APPROVED = 'Approved'

    STATUS_CHOICES = [
        (REQUESTED, 'Requested'),
        (APPROVED, 'Approved'),
    ]

    description = models.TextField()
    file_type = models.CharField(max_length=100)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_requests')
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=REQUESTED)

