from django.shortcuts import render
from django.http import HttpResponse
from .models import Band,Listing


# Create your views here.
def hello(request):
    bands=Band.objects.all()
    bands_dic={
        'first_band':bands[0],
        'second_band':bands[1],
        'third_band':bands[2]
    }
    return render(request,"hello.html",{'bands':bands})


def band(request):
    bands=Band.Objects.all()
    return render(request,"band.html",{'bands':bands})




def listing(request):
    listings=Listing.objects.all()
    return render(request,"listing.html",{'listings':listings})



def about(request):
     return render(request,"contact.html")


def contact(request):
    return render(request,"contact.html")
