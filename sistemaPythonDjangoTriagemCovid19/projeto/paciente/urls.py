from django.conf.urls import url

from .views import PacienteListView, PacienteCreateView
from .views import PacienteUpdateView, PacienteDeleteView


urlpatterns = [
	url(r'list/$', PacienteListView.as_view(), name='paciente_list'),
	url(r'cad/$', PacienteCreateView.as_view(), name='paciente_create'),
	url(r'(?P<pk>\d+)/$', PacienteUpdateView.as_view(), name='paciente_update'),
	url(r'(?P<pk>\d+)/delete/$', PacienteDeleteView.as_view(), name='paciente_delete'), 
]
