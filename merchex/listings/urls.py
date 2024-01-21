from django.urls import path
from listings import views
urlpatterns = [
    path('about',views.hello,name='about'),
    path('hello/',views.hello,name='hello'),
    path('about/',views.about,name='about'),
    path('listings/',views.listing,name='listings')
]

