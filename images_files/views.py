from django.shortcuts import render
from .models import ImageFile
# Create your views here.

def pdfs(request):
    imagepdfs=ImageFile.objects.all()
    for i in imagepdfs:
        print('------>',i.title,i.image_pdf.url)
    context={'imagepdfs':imagepdfs}
    return render(
        request=request,
        template_name='pdfs.html',
        context=context)

def pdf_page(request,pk):
    imagepdf=ImageFile.objects.get(id=pk)
    context={'imagepdf':imagepdf}
    return render(request=request,template_name='pdf_page.html',context=context)
    

def index(request):
    pdfs=ImageFile.objects.all()

    for i in pdfs:
        print('------>',i.name,i.image_pdf.url)
    context={'pdfs':pdfs}


    return render(
        request=request,
        template_name='index.html',
        context=context)