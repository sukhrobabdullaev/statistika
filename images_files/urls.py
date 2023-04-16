from django.urls import path
from .views import pdfs,pdf_page,index


urlpatterns = [
    path('pdfs/',pdfs,name='pdfs'),
    path('',index,name='index'),
    
    path('pdf_page/<int:pk>/',pdf_page,name='pdf_page'),
]