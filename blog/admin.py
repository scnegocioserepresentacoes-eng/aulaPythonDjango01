from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('titulo','criado_em') 

