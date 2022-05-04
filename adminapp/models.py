from django.db import models

# Create your models here.
class home_wallpaper(models.Model):
    wallpaper_text=models.CharField(max_length=150)
    wallpaper_pic=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
   
