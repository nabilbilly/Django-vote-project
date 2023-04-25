from django.db import models  
from django.forms import fields  
from .models import Image  
from django import forms  
  
  

class ImageForm(forms.ModelForm):
    class Meta:
         # To specify the model to be used to create form  
        model = Image
        # It includes all the fields of model  
        fields = ['titel','image']