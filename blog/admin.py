from .models import Post, Category
from django.contrib import admin
import django.apps
from django.contrib.contenttypes.models import ContentType

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    # fields = ['title', ('author', 'slug')]
    # above we grouped author and slug together

    fieldsets = (
        ('Main Section', {
            'fields': ('title', 'author'),
            'description': 'just a simple description',
        }),
        ('Section two', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Post, PostAdmin)
