from rest_framework.routers import SimpleRouter
from comments.views import CommentViewSet

router = SimpleRouter()

router.register('comment', CommentViewSet)


urlpatterns = []

urlpatterns += router.urls