from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
admin.site.index_title = 'سایت لباس فروشی'
admin.site.site_header = 'پنل ادمین سایت لباس فروشی'
admin.site.site_title = 'تایتل سایت'
