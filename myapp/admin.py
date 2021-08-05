from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Comment)


class PostImageAdmin(admin.StackedInline):
    model=Post_image

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

@admin.register(Post_image)
class PostImageAdmin(admin.ModelAdmin):
    pass


