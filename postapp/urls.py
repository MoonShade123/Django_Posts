from .views import RegistrationAPIView, LoginAPIView, PostAPIView
from django.urls import re_path

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^posts/?$', PostAPIView.as_view(), name='user_posts'),
]
