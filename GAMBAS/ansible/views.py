from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import os
import json
# Create your views here.
def index(request):
    return render(request, 'ansible/ansible.html', {})


def push_file(request):
    """
    View for uploading a file.
    """
    # Get the list of firewalls.
    firewalls = json.load(open('static/fw.json'))
    if request.method == 'POST':
        print(request.POST)
        selected_firewalls = request.POST.getlist('firewalls[]')
        # Print the selected firewalls
        print(selected_firewalls)
        # Check if the file is valid.
        if not request.FILES['file'].content_type == 'text/plain':
            return HttpResponse('File must be a text file.', status=415)

        # Save the file.
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        if save_file(request):
            return render(request, 'ansible/push_file.html', {'form': form, 'file' : True, 'file_name' : file, 'firewalls': firewalls})
        else:
            return HttpResponse('Error saving file.', status=500)

    else:
        form = UploadFileForm()
    return render(request, 'ansible/push_file.html', {'form': form, 'file' : False, 'firewalls': firewalls})




def save_file(request):
    """
    Save the uploaded file.
    """
    file = request.FILES['file']
    filename = file.name
    file_extension = file.name.split('.')[-1]

    # Save the file to the filesystem.
    print(os.path)
    with open(os.path.join('media', filename), 'wb') as f:
        f.write(file.file.read())

    return True
