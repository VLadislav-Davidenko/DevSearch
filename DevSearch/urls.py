from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projects.urls")),
]

# Here we grabed the MEDIA URL and conneted it to MEDIA ROOT to render our images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
