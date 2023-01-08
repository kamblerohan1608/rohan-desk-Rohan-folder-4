from django.shortcuts import render
from . import models

# Create your views here.
def home(request):

    category=models.Category.objects.all()
    images=models.Images.objects.all()

    
    data= {'category':category,'images':images}

    return render(request,'home/home.html',data)

def category(request,id ):#its a dynamic function ---its used to display specific images

    cats=models.Category.objects.all()
    category=models.Category.objects.get(id=id)
    images=models.Images.objects.filter(cat=category)

    
    data= {'category':cats,'images':images}

    return render(request,'home/home.html',data)