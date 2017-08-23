from rest_framework import viewsets

from routes.serializers import RouteSerializer
from routes.models import Route

class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows routes to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
