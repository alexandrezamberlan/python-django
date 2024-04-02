from django.conf.urls import url

from .views import ConsultaListView, ConsultaCreateView
from .views import ConsultaUpdateView, ConsultaDeleteView


urlpatterns = [
 	url(r'list/$', ConsultaListView.as_view(), name='consulta_list'),
	url(r'cad/$', ConsultaCreateView.as_view(), name='consulta_create'),
	url(r'(?P<pk>\d+)/$', ConsultaUpdateView.as_view(), name='consulta_update'),
	url(r'(?P<pk>\d+)/delete/$', ConsultaDeleteView.as_view(), name='consulta_delete'), 
]
