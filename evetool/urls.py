from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'evetool.views.home', name='home'),
    url(r'^', include('users.urls')),
    url(r'^', include('apis.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
