from django.contrib import admin
from django.urls import path
from blog.admin import blog_site

urlpatterns = [
    path('blogAdmin/', blog_site.urls),
    path('admin/', admin.site.urls),
]
# admin.site.index_title = 'سایت لباس فروشی'
# admin.site.site_header = 'پنل ادمین سایت لباس فروشی'
# admin.site.site_title = 'تایتل سایت'
