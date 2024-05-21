from __future__ import unicode_literals
from django.urls import path
from .views import HomeView, AboutView, HomeRedirectView

urlpatterns = [
   path('', HomeRedirectView.as_view(), name='home_redirect'),
   path('home', HomeView.as_view(), name='home'),
   path('about', AboutView.as_view(), name='about'),
]
