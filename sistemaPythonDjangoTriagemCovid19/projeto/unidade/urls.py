from django.conf.urls import url

from .views import UnidadeListView, UnidadeCreateView
from .views import UnidadeUpdateView, UnidadeDeleteView


urlpatterns = [
	url(r'list/$', UnidadeListView.as_view(), name='unidade_list'),
	url(r'cad/$', UnidadeCreateView.as_view(), name='unidade_create'),
	url(r'(?P<pk>\d+)/$', UnidadeUpdateView.as_view(), name='unidade_update'),
	url(r'(?P<pk>\d+)/delete/$', UnidadeDeleteView.as_view(), name='unidade_delete'), 
]
