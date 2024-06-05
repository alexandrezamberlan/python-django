from django.urls import path

from .views import InstituicaoListView, InstituicaoCreateView
from .views import InstituicaoUpdateView, InstituicaoDeleteView


urlpatterns = [
	path('list/', InstituicaoListView.as_view(), name='instituicao_list'),
	path('cad/', InstituicaoCreateView.as_view(), name='instituicao_create'),
	path('<slug:slug>/', InstituicaoUpdateView.as_view(), name='instituicao_update'),
	path('<slug:slug>/delete/', InstituicaoDeleteView.as_view(), name='instituicao_delete'), 
]
 