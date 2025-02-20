from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# first create the static file manually
# then configure what you need in settings.py
# then the above url and finaly
# run "python manage.py collectstatic"
# then create templates manually
# again templates configurations in settings.py
