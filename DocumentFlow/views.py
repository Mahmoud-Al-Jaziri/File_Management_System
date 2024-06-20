from django.shortcuts import render,redirect,get_object_or_404
from .forms import FileUploadForm, FileRequestForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import File, FileRequest
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .decorators import unauthenticated_user
from django.urls import reverse
from django.http import FileResponse
from django.conf import settings
import os
from django.http import HttpResponse

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('file_list')
        else:
            messages.info(request, 'Username OR password is incorrect')
            

    context = {}
    return render(request,'DocumentFlow/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.uploaded_by = request.user
            file_instance.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'DocumentFlow/upload_file.html', {'form': form})


@login_required(login_url='loginPage')
def file_list(request):
    files = File.objects.all()
    return render(request, 'DocumentFlow/file_list.html', {'files': files})


@login_required(login_url='loginPage')
def file_detail(request, pk):
    file = get_object_or_404(File, pk=pk)
    file_url = reverse('serve_file', args=[file.pk])
    return render(request, 'DocumentFlow/file_detail.html', {'file': file, 'file_url': file_url,})

@login_required
def serve_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
    
    return FileResponse(open(file_path, 'rb'), as_attachment=False, content_type='application/octet-stream')


@login_required
def review(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.status = 'Needs Manager Review'
    file.save()
    return redirect('file_list')

@login_required
def ask_for_update(request, pk):
    file = get_object_or_404(File, pk=pk)
    if request.method == 'POST':
        notes = request.POST.get('notes', '')
        file.notes = notes
        file.status = 'Needs Update'
        file.save()
        return redirect('file_list')
    return render(request, 'DocumentFlow/ask_for_update.html', {'file': file})

@login_required
def reject_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    if request.method == 'POST':
        rejection_notes = request.POST.get('rejection_notes', '')
        file.rejection_notes = rejection_notes
        file.status = 'Rejected'
        file.save()
        return redirect('file_list')
    return render(request, 'DocumentFlow/reject_file.html', {'file': file})


@login_required
def manager_file_list(request):
    if request.user.groups.filter(name='Manager').exists():
        files = File.objects.filter(status='Needs Manager Review')
        return render(request, 'DocumentFlow/manager_file_list.html', {'files': files})
    else:
        return HttpResponse('You are not authorized to view this page')


@login_required
def update_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            file.status = 'Updated'
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm(instance=file)
    return render(request, 'DocumentFlow/update_file.html', {'form': form, 'file': file})


@login_required
def request_file(request):
    if request.method == 'POST':
        form = FileRequestForm(request.POST)
        if form.is_valid():
            file_request = form.save(commit=False)
            file_request.requested_by = request.user 
            file_request.save()
            return redirect('file_request_list')
    else:
        form = FileRequestForm()
    return render(request, 'DocumentFlow/request_file.html', {'form': form})


@login_required
def file_request_list(request):
    requests = FileRequest.objects.all()
    return render(request, 'DocumentFlow/file_request_list.html', {'requests': requests})


@login_required
def accept(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.status = 'Accepted'
    file.save()
    user = request.user
    if user == "Manager":
        return redirect('manager_file_list')
    else:
        return redirect('file_list')

@login_required
def accepted_file_list(request):
    files = File.objects.filter(status='Accepted')
    return render(request, 'DocumentFlow/accepted_file_list.html', {'files': files})

@login_required
def supervisor_review(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.status = 'Needs Supervisor Review'
    file.save()
    return redirect('file_list')

