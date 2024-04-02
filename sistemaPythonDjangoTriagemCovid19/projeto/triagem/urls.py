from django.conf.urls import url

from .views import TriagemListView, TriagemMinhasUnidadesListView, TriagemCreateView
from .views import TriagemUpdateView, TriagemDeleteView


urlpatterns = [
 	url(r'list/$', TriagemListView.as_view(), name='triagem_list'),
	url(r'minhas-triagens/$', TriagemMinhasUnidadesListView.as_view(), name='triagem_minhas_unidades'),
	url(r'cad/$', TriagemCreateView.as_view(), name='triagem_create'),
	url(r'(?P<pk>\d+)/$', TriagemUpdateView.as_view(), name='triagem_update'),
	url(r'(?P<pk>\d+)/delete/$', TriagemDeleteView.as_view(), name='triagem_delete'), 
]
