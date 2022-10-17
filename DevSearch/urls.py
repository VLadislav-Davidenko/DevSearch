from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include("projects.urls")),
    path('', include("users.urls")),

]

# Here we grabed the MEDIA URL and conneted it to MEDIA ROOT to render our images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# To allow use static files while not in debuging mode
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)