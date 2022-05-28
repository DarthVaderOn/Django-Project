from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from profile_app.views.authorization import Authorization
from profile_app.views.logout import LogoutUser
from profile_app.views.profile import Profile_User
from profile_app.views.registration import RegistrationView
from profile_app.views.update_profile import user_redaction


urlpatterns = [
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('authorization', Authorization.as_view(), name='auth_page'),
    path('logout', LogoutUser.as_view(), name='logout_page'),
    path('profile/', Profile_User.as_view(), name='profile_page'),
    path('profile/update/', user_redaction, name='update_profile_page'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()