from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from tags_app.api.views.tags import TagView


urlpatterns = [
    path('api/tag', TagView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='api-tags'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()