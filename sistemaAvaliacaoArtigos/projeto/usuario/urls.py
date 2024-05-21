# from django.conf.urls import url
from django.urls import path

from .views import UsuarioListView, UsuarioCreateView
from .views import UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
	path('list/$', UsuarioListView.as_view(), name='usuario_list'),
	path('cad/$', UsuarioCreateView.as_view(), name='usuario_create'),
	path('<slug:slug>/', UsuarioUpdateView.as_view(), name='usuario_update'),
	path('<slug:slug>/delete/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]
