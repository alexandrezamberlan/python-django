from django.urls import path

from .views import EventoListView, EventoCreateView
from .views import EventoUpdateView, EventoDeleteView


urlpatterns = [
	path('list/', EventoListView.as_view(), name='evento_list'),
	path('cad/', EventoCreateView.as_view(), name='evento_create'),
	path('<slug:slug>/', EventoUpdateView.as_view(), name='evento_update'),
	path('<slug:slug>/delete/', EventoDeleteView.as_view(), name='evento_delete'), 
]
 