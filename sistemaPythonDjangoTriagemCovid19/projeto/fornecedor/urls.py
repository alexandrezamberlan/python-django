from django.conf.urls import url

from .views import FornecedorListView, FornecedorCreateView
from .views import FornecedorUpdateView, FornecedorDeleteView


urlpatterns = [
	url(r'list/$', FornecedorListView.as_view(), name='fornecedor_list'),
	url(r'cad/$', FornecedorCreateView.as_view(), name='fornecedor_create'),
	url(r'(?P<pk>\d+)/$', FornecedorUpdateView.as_view(), name='fornecedor_update'),
	url(r'(?P<pk>\d+)/delete/$', FornecedorDeleteView.as_view(), name='fornecedor_delete'), 
]
