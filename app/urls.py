from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"

urlpatterns = [
    path("", views.Image_Upload.as_view(), name="home"),
    path("process_image/", views.process_image, name="process_image")
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
