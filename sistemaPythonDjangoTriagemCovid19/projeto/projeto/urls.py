from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'usuario/', include('usuario.urls')),
    url(r'unidade/', include('unidade.urls')),
    url(r'triagem/', include('triagem.urls')),
    url(r'medicamento/', include('medicamento.urls')),
    url(r'consulta/', include('consulta.urls')),
    url(r'paciente/', include('paciente.urls')),
    url(r'fornecedor/', include('fornecedor.urls')),
   
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)   