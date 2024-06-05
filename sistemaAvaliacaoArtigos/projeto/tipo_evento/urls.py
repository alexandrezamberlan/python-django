from django.urls import path

from .views import TipoEventoListView, TipoEventoCreateView
from .views import TipoEventoUpdateView, TipoEventoDeleteView


urlpatterns = [
	path('list/', TipoEventoListView.as_view(), name='tipo_evento_list'),
	path('cad/', TipoEventoCreateView.as_view(), name='tipo_evento_create'),
	path('<slug:slug>/', TipoEventoUpdateView.as_view(), name='tipo_evento_update'),
	path('<slug:slug>/delete/', TipoEventoDeleteView.as_view(), name='tipo_evento_delete'), 
]
 