from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from media_app.api.views.publications import PostsView
from media_app.views.posts import PostCreate


urlpatterns = [
    path('post', PostCreate.as_view(), name='post_page'),
    path('api/posts', PostsView.as_view({'get': 'list', 'post': 'create'}), name='api-posts'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()