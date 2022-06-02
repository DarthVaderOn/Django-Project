from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from likes_app.api.views.likes import LikePostsView, LikeCommentsView


urlpatterns = [
    path('api/likes', LikePostsView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='api-likeposts'),
path('api/likes', LikeCommentsView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='api-likecomments'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()