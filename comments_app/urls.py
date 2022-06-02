from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from comments_app.api.views.comments import CommentsView
from django.urls import path


urlpatterns = [
    path('api/comments', CommentsView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='api-comments'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()