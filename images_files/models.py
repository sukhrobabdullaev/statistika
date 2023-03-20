from django.db import models
from account.models import Account
from common.models import BaseModel
# Create your models here.
class ImageFile(BaseModel):
    image_pdf=models.FileField()
    title=models.CharField(max_length=250,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.name)
    class Meta:
            verbose_name='ImageFile'
            verbose_name_plural='ImageFiles'


class ImagePart(models.Model):
    imagefile=models.ForeignKey(ImageFile,related_name='imageparts', on_delete=models.SET_NULL,null=True)
    oneimage=models.FileField()
    qrcode_image=models.ImageField()
    title=models.CharField(max_length=250,null=True,blank=True)
    
    def __str__(self):
         return self.title

    class Meta:
        verbose_name='ImagePart'
        verbose_name_plural='ImageParts'
        

    