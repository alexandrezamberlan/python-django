from django.conf.urls import url

from .views import MedicamentoListView, MedicamentoCreateView
from .views import MedicamentoUpdateView, MedicamentoDeleteView


urlpatterns = [
	url(r'list/$', MedicamentoListView.as_view(), name='medicamento_list'),
	url(r'cad/$', MedicamentoCreateView.as_view(), name='medicamento_create'),
	url(r'(?P<pk>\d+)/$', MedicamentoUpdateView.as_view(), name='medicamento_update'),
	url(r'(?P<pk>\d+)/delete/$', MedicamentoDeleteView.as_view(), name='medicamento_delete'), 
]
