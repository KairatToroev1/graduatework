from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny

from comments.models import Comment
from comments.serializers import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny ]