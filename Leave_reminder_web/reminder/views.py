import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import LeaveForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import date

# Create your views here.


def dataview(request):
    form = LeaveForm()
    if request.method == "POST":
        form = LeaveForm(request.POST, request.FILES)
        if form.is_valid():
            
            #GETTING THE PATH FOR THE CSV FILES FROM THE SETTINGS
            directorypath = settings.MEDIA_ROOT
            
            print(settings.STATICFILES_DIRS[0])
            
            #DELETING ANY FILES IF THERE ARE ANY IN THE FOLDER
            for the_file in os.listdir(directorypath):
                file_path = os.path.join(directorypath, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    #elif os.path.isdir(file_path): shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            
            #INITIATING THE FILE STORAGE SYSTEM
            fs = FileSystemStorage()
            leave_file = request.FILES['leave_file']
        
            
            fs.save('Leave_file.csv', leave_file)
                   
            return render(request, 'final.html')
    
    
    return render(request, 'dataview.html', {'form' : form })

