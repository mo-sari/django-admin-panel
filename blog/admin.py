from .models import Post, Category
from django.contrib import admin
import django.apps
from django.contrib.contenttypes.models import ContentType

admin.site.register(Category)

# these below are the two different ways of doing the same thing
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'author']


# admin.site.register(Post, PostAdmin)
# the above way or below

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'author']
# =======================================================
# this is the way to register all the models at once

models = django.apps.apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        continue


admin.site.unregister(ContentType)
