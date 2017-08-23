from rest_framework import serializers
from routes.models import Route


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('name', 'source', 'link', 'category')
