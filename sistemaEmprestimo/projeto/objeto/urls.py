from django.conf.urls import url

from .views import ObjetoListView, ObjetoCreateView
from .views import ObjetoUpdateView, ObjetoDeleteView


urlpatterns = [
	url(r'list/$', ObjetoListView.as_view(), name='objeto_list'),
	url(r'cad/$', ObjetoCreateView.as_view(), name='objeto_create'),
	url(r'(?P<pk>\d+)/$', ObjetoUpdateView.as_view(), name='objeto_update'),
	url(r'(?P<pk>\d+)/delete/$', ObjetoDeleteView.as_view(), name='objeto_delete'), 
]
