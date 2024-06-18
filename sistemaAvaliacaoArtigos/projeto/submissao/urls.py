from django.urls import path

from .views import SubmissaoListView, SubmissaoCreateView
from .views import SubmissaoUpdateView, SubmissaoDeleteView


urlpatterns = [
	path('list/', SubmissaoListView.as_view(), name='submissao_list'),
	path('cad/', SubmissaoCreateView.as_view(), name='submissao_create'),
	path('<slug:slug>/', SubmissaoUpdateView.as_view(), name='submissao_update'),
	path('<slug:slug>/delete/', SubmissaoDeleteView.as_view(), name='submissao_delete'), 
]
 