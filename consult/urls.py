
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

# handler404 = 'main.views.error'

urlpatterns = [
    path('myconsult/admin/page/', admin.site.urls),
    path('', include('main.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


