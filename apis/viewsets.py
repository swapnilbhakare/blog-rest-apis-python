from rest_framework import viewsets
from . import models
from . import serializer

class PostsViewset(viewsets.ModelViewSet):
    queryset = models.Posts.objects.all()
    serializer_class = serializer.PostsSerializer