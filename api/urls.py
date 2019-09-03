from django.urls import include, path, re_path
from rest_auth.views import PasswordResetConfirmView, PasswordResetView

urlpatterns = [
    re_path('rest-auth/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    re_path(
        'rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),  # the token at the end of this URL is from the email, not the authentication token from logging in or signing up
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),  # supported endpoint: create account

    path('users/', include('users.urls')),
]
