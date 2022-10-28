from django.contrib import admin
from .models import PostModel, Comments
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_create', 'author', 'content')
admin.site.register(PostModel, PostModelAdmin)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content')
admin.site.register(Comments, CommentsAdmin)

