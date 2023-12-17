from django.urls import path
from apps.scrape_apps.views import ManualScrape

urlpatterns = [
    path('trigger-scrape', ManualScrape.as_view(), name='Manual-Scrape'),
]