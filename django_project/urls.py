from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import notifications.urls



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('match/', include('match.urls')),
    path('user/', include('user.urls')),
    path('', include('blog.urls')),
    path('messages/', include('chat.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

