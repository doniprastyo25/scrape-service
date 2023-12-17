from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scraping/', include('apps.scrape_apps.urls'))
]
