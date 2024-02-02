from django.urls import path
from listings import views
urlpatterns = [
    path('about',views.about,name='about'),
    path('home/',views.base,name='home'),
    path('email_sent/',views.email_sent,name='email_sent'),
    path('contact/',views.contact,name='contact'),
    path('bands/',views.band_list,name='band_list'),
    path('bands/<int:band_id>/',views.band_detail,name="band_detail"),
    path('bands/add/',views.band_create,name="band_create"),
    path('listings/add/',views.listing_create,name="listing_create"),
    path('listings/',views.listing_list,name='listing_list'),
    path('listings/<int:listing_id>/',views.listing_detail,name="listing_detail"),
]

