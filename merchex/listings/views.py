from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse,Http404
from .models import Band,Listing


# Create your views here.
def band_list(request):
    bands=Band.objects.all()
    return render(request,"band_list.html",{'bands':bands})


def base(request):
    return render(request,"base.html")



def listing_list(request):
    listings=Listing.objects.all()
    return render(request,"listing_list.html",{'listings':listings})



def about(request):
     return render(request,"contact.html")


def contact(request):
    return render(request,"contact.html")

def band_detail(request,band_id:int):
    try:
        band = Band.objects.get(id=band_id)
        return render(request, "band_detail.html", {'band': band})
    except Band.DoesNotExist:
        return render(request, "404.html", {'message': "Le groupe demandée n'existe pas."})

def listing_detail(request,listing_id:int):
    try:
        listing = Listing.objects.get(id=listing_id)
        band_id=listing.band.id
        return render(request, "listing_detail.html", {'listing':listing,'band_id':band_id})
    except Listing.DoesNotExist:
        return render(request, "404.html", {'message': "L ' article demandée n'existe pas."})

