from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "post_title",
        "post_posted_at",
        "post_updated_at",
    )
