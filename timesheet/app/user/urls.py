from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_pattern
from . import views

urlpatterns = [
    
    url(r'^users/',views.userList.as_view()),
]