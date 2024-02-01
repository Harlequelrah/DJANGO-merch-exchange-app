from django.urls import path
from listings import views
urlpatterns = [
    path('about',views.about,name='about'),
    path('base/',views.base,name='home'),
    path('contact',views.about,name='contact'),
    path('bands/',views.band_list,name='band_list'),
    path('bands/<int:band_id>/',views.band_detail,name="band_detail"),
    path('listings/',views.listing_list,name='listing_list'),
    path('listings/<int:listing_id>/',views.listing_detail,name="listing_detail"),
]

