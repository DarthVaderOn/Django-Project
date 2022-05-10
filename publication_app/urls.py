from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from publication_app.views.registration import RegistrationView
from publication_app.views.main import MainPageView
from publication_app.views.authorization import Authorization_page
# from publication_app.forms.profile import UpdateProfileForm, UpdateProfileAvaForm
# from publication_app.views.profile import Profile_user
# from publication_app.views.posts import PostCreateView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('authorization', Authorization_page.as_view(), name='auth_page'),
    # path('profile/', Profile_user.as_view(), name='profile'),
    # path('profile/update/<int:pk>/', UpdateProfileForm.as_view(), name='update_profile'),
    # path('profile/update/avatar/<int:pk>/', UpdateProfileAvaForm.as_view(), name='update_avatar'),
    # path('post/create/', PostCreateView.as_view(), name='post_create_url'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()