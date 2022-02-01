from .views import RegistrationAPIView, LoginAPIView, PostAPIView, UserAPIView, LikeAPIView
from django.urls import re_path

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^posts/?$', PostAPIView.as_view(), name='user_posts'),
    re_path(r'^users/?$', UserAPIView.as_view(), name='users'),
    re_path(r'^like/?$', LikeAPIView.as_view(), name='like'),
]
