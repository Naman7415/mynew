from django.shortcuts import render,HttpResponse
from file.forms import FileFieldForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# from .somewhere import handle_uploaded_file
# Create your views here.

# def createfile(request):
#     if request.method == 'POST':
#         form=UploadForm(request.POST,request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES["file"])
#             return HttpResponse('success')
    
#     else:
#         form=UploadForm()
#     return render(request,'upload.html',{'form':form})
        
@csrf_protect
def upload_files(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            files=request.FILES.getlist('files')
            for i in files:
                destination = open('filess.txt' + i.name, 'wb')
                for chunk in i.chunks():
                    destination.write(chunk)
                destination.close()
            return HttpResponse('success_url')
    else:
        form = FileFieldForm()
        print('that is called',form)

    return render(request, 'upload.html', {'form': form})
