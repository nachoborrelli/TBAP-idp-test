from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from users.register_views import EmailVerification
from dj_rest_auth.registration.views import ResendEmailVerificationView, RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from users.views import UserInfo

urlpatterns = [
    path('admin/', admin.site.urls),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # Auth
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    re_path("signup/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", EmailVerification.as_view(), name='account_confirm_email'),
    path('account-email-verification-sent/', EmailVerification.as_view(), name='account_email_verification_sent'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    path('userinfo/', UserInfo.as_view(), name='userinfo'),
    # Apps
    path('api/users/', include('users.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
