from django.urls import path

from .views import AvisoListView, AvisoCreateView
from .views import AvisoUpdateView, AvisoDeleteView, AvisoEnviaEmail, AvisoListIFrameView


# urlpatterns = [
# 	url(r'list/$', AvisoListView.as_view(), name='aviso_list'),
# 	url(r'cad/$', AvisoCreateView.as_view(), name='aviso_create'),
# 	url(r'(?P<pk>\d+)/$', AvisoUpdateView.as_view(), name='aviso_update'),
# 	url(r'(?P<pk>\d+)/delete/$', AvisoDeleteView.as_view(), name='aviso_delete'),
# 	url(r'(?P<pk>\d+)/envia-email/$', AvisoEnviaEmail.as_view(), name='aviso_envia_email'),
# 	url(r'list/iframe$', AvisoListIFrameView.as_view(), name='aviso_list_iframe'),
# ]

urlpatterns = [
	path('list/', AvisoListView.as_view(), name='aviso_list'),
	path('cad/', AvisoCreateView.as_view(), name='aviso_create'),
	path('<slug:slug>/', AvisoUpdateView.as_view(), name='aviso_update'),
	path('<slug:slug>/delete/', AvisoDeleteView.as_view(), name='aviso_delete'), 
 	path('<slug:slug>/envia-email/', AvisoEnviaEmail.as_view(), name='aviso_envia_email'),
	path('list/iframe', AvisoListIFrameView.as_view(), name='aviso_list_iframe'),
]
 