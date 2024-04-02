from __future__ import unicode_literals
from django.conf.urls import url
from .views import HomeView, AboutView, HomeRedirectView

urlpatterns = [
   url(r'^$', HomeRedirectView.as_view(), name='home_redirect'),
   url(r'^home$', HomeView.as_view(), name='home'),
   url(r'^about$', AboutView.as_view(), name='about'),
]