from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.title
    def comments_count(self):
        return self.comments_set.all().count()
    def comments(self):
        return self.comments_set.all()
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    def __str__(self):
        return self.content