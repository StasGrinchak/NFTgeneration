from django.shortcuts import render
import os #.path
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.


def createIMG(request):
    form =SubscriberForm(request.POST or None)
    if request.method == 'POST':
        new_form = form.save()
        data = form.cleaned_data
        # Запускаем скрипт для Создания картинки
        all =Subscriber.objects.all()
    form =SubscriberForm()
    return render(request, 'create.html',locals())




def upload(request):
    if request.method == 'POST':
        upload_file= request.FILES['document']
        fs = FileSystemStorage()
        fs.save(upload_file.name,upload_file)
        # Запустить скрипт по обнаружению ТОКЕНА на картинке
    return render(request,'generation/upload.html')

def download(request,fl):
    direct =''
    all_files=os.listdir(direct)
    for file in all_files:
        fl = open(direct + file,'rb')
        response = HttpResponse(fl.read(),content_type=file)
        response['Content-Disposition']="attachment; filename=%s"
    return response