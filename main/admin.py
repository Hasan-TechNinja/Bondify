from django.contrib import admin
from . models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'create_post', 'image', 'video', 'created', 'updated', 'status'
    )
admin.site.register(Post, PostAdmin)