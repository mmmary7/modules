from django.urls import path
from .views import index, top_sellers, advertisement_post
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers.html/', top_sellers, name='top-sellers'),
    path('advertisement-post.html/', advertisement_post, name='advertisement-post')
]

if settings.DEBAG:
    urlpatterns = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)