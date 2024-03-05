from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound,HttpResponse,Http404
from .models import Band,Listing
from .forms import ContactUsForm,BandForm,ListingForm
from django.core.mail import send_mail
from django.contrib import messages


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
    return render(request,"about.html")

def email_sent(request):
    return render(request,"email_sent.html")


def contact(request,*args,**kwargs):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data["name"]or "anonymous"} Via Merchex Contact Us Form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=['degbovimax19@gmail.com'],
            )
            return redirect(email_sent)

    else:form=ContactUsForm()

    return render(request,"contact.html",{'form':form})
 # print('La méthode de requête est : ', request.method)
    # print('Les données POST sont : ', request.POST)


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

def band_create(request):
    if request.method=='POST':
        form=BandForm(request.POST)
        if form.is_valid():
            band=form.save()
            messages.success(request, 'Opération réussie !')
            return redirect('band_detail',band.id)
    else:form=BandForm()
    return render(request,"band_create.html",{'form':form})


def listing_create(request):
    if request.method=='POST':
        form=ListingForm(request.POST)
        if form.is_valid():
            listing=form.save()
            messages.success(request, 'Opération réussie !')
            return redirect('listing_detail',listing.id)
    else:form=ListingForm()
    return render(request,"band_create.html",{'form':form})

def band_update(request,band_id):
    band=Band.objects.get(id=band_id)
    if request.method=='POST':

        form=BandForm(request.POST,instance=band)
        if form.is_valid():
            band=form.save()
            messages.success(request, 'Opération réussie !')
            return redirect('band_detail',band_id)
    else:form=BandForm(instance=band)
    return render(request,"band_update.html",{'form':form})



def listing_update(request,listing_id):
    listing=Listing.objects.get(id=listing_id)
    if request.method=='POST':

        form=ListingForm(request.POST,instance=listing)
        if form.is_valid():
            listing=form.save()
            messages.success(request, 'Opération réussie !')
            return redirect('listing_detail',listing_id)
    else:form=ListingForm(instance=listing)
    return render(request,"listing_update.html",{'form':form})

def band_delete(request,band_id):
    band=Band.objects.get(id=band_id)
    if request.method=='POST':
        band.delete()
        messages.success(request, 'Opération réussie !')
        return redirect('band_list')
    return render(request,"band_delete.html",{'band':band})

def listing_delete(request,listing_id):
    listing=Listing.objects.get(id=listing_id)
    if request.method=='POST':
        listing.delete()
        messages.success(request, 'Opération réussie !')
        return redirect('listing_list')
    return render(request,"listing_delete.html",{'listing':listing})

