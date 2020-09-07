from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', include('frontend.urls')),
    #path('', include('main.urls')),
    path('', include('accounts.urls')),

    path('', include('core.urls')),
    path('', include('authentication.urls')),

    path('api/', include('requests.urls')),
    
    path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/backups/', include('dbbackup_ui.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
