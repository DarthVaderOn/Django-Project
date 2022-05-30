from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from publication_app.views.main import MainPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('tag/<int:tag_id>/', MainPageView.get_tags,),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()