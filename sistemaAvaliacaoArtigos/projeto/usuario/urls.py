# from django.conf.urls import url
from django.urls import path

from .views import UsuarioListView, UsuarioCreateView
from .views import UsuarioUpdateView, UsuarioDeleteView
from .views import UsuarioRegisterSuccessView, UsuarioRegisterSuccessFalhaEmailView, UsuarioRegisterActivateView, UsuarioRegisterView

urlpatterns = [
	path('list/', UsuarioListView.as_view(), name='usuario_list'),
	path('cad/', UsuarioCreateView.as_view(), name='usuario_create'),
	path('<slug:slug>/', UsuarioUpdateView.as_view(), name='usuario_update'),
	path('<slug:slug>/delete/', UsuarioDeleteView.as_view(), name='usuario_delete'),
 
 	path('register/success/',UsuarioRegisterSuccessView.as_view(),name='usuario_register_success'),
	path('register/success_falha_email/',UsuarioRegisterSuccessFalhaEmailView.as_view(),name='usuario_register_success_falha_email'),
	path('register/<slug:slug>/activate/', UsuarioRegisterActivateView.as_view(), name='usuario_register_activate'),
	path('register', UsuarioRegisterView.as_view(), name='usuario_register'),
]
