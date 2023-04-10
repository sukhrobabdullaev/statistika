from django.shortcuts import render
from .models import ImageFile
# Create your views here.

def index(request):
    imagepdfs=ImageFile.objects.all()
    for i in imagepdfs:
        print('------>',i.title,i.image_pdf.url)
    context={'imagepdfs':imagepdfs}
    return render(request=request,template_name='index.html',context=context)