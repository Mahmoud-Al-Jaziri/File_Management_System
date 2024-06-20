from django.forms import ModelForm
from .models import Employee, File, FileRequest
from django import forms

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'
		exclude = ['user']
		
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'file_type', 'description', 'assigned_to']
        
class FileRequestForm(forms.ModelForm):
    class Meta:
        model = FileRequest
        fields = ['description', 'file_type']