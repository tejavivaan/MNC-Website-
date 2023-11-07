from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('sinup/',views.sinup,name="sinup"),
    path('sinin/',views.sinin,name='sinin'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),

]