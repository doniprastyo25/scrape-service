from rest_framework.views import APIView
from rest_framework.response import Response
from apps.scrape_apps.helper.scrape_platform import linkedin, jobstreet

class ManualScrape(APIView):
    def get(self, request, format=None):
        data = linkedin.Linkedin()
        return Response(data.result_scrape)
    