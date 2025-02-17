from .models import Post
from django.contrib import admin


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'


blog_site = BlogAdminArea(name='BlogAdmin')
blog_site.register(Post)
admin.site.register(Post)
