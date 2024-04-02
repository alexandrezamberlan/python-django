from django.conf.urls import url

from .views import EmprestimoListView, EmprestimoCreateView
from .views import EmprestimoUpdateView, EmprestimoDeleteView


urlpatterns = [
	url(r'list/$', EmprestimoListView.as_view(), name='emprestimo_list'),
	url(r'cad/$', EmprestimoCreateView.as_view(), name='emprestimo_create'),
	url(r'(?P<pk>\d+)/$', EmprestimoUpdateView.as_view(), name='emprestimo_update'),
	url(r'(?P<pk>\d+)/delete/$', EmprestimoDeleteView.as_view(), name='emprestimo_delete'), 
]
