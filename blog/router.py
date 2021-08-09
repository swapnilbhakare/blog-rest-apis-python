from apis.viewsets import PostsViewset
from rest_framework import routers
router = routers.DefaultRouter()

router.register('posts',PostsViewset)