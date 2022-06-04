from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from publication_app.api.views.router import api_router
from publication_app.views.main import MainPageView
from publication_app.views.posts import PostCreate


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('tag/<int:tag_id>/', MainPageView.get_tags, name='get_tags'),
    path('post', PostCreate.as_view(), name='post_page'),
    path('api/', include(api_router.urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()