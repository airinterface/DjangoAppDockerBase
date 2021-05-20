from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import StorySerializer
from .models import Story

class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Story.objects.all().order_by('-index')
    serializer_class = StorySerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        serializer = super(StoryViewSet, self).list( request, *args, **kwargs )
        ret = serializer.data["results"]
        return Response( ret )

