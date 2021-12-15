from django.db import models
from place.models import Tour
from django.contrib.auth import get_user_model


User = get_user_model()



class Comment(models.Model):
    post = models.ForeignKey(Tour, on_delete=models.SET_NULL,
                             null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments",
                               verbose_name="Автор поста")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # class Meta:
