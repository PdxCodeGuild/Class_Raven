from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView #opens the catalog page by default
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)          #CHECK LATER

