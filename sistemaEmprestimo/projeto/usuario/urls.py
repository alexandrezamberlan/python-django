from django.conf.urls import url

from .views import UsuarioListView, UsuarioCreateView
from .views import UsuarioUpdateView, UsuarioDeleteView
from .views import UsuarioRegisterView, UsuarioRegisterSuccessView, UsuarioRegisterActivateView

urlpatterns = [
	url(r'list/$', UsuarioListView.as_view(), name='usuario_list'),
	url(r'cad/$', UsuarioCreateView.as_view(), name='usuario_create'),
	url(r'(?P<pk>\d+)/$', UsuarioUpdateView.as_view(), name='usuario_update'),
	url(r'(?P<pk>\d+)/delete/$', UsuarioDeleteView.as_view(), name='usuario_delete'),
	url(r'register/success/',UsuarioRegisterSuccessView.as_view(),name='usuario_register_success'),
	url(r'register/(?P<slug>[-\w\d]+)/activate/', UsuarioRegisterActivateView.as_view(), name='usuario_register_activate'),
	url(r'register', UsuarioRegisterView.as_view(), name='usuario_register'), 
]