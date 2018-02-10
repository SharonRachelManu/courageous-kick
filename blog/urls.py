from django.conf.urls import url

from .views import createPost

urlpatterns = [
    url(r'create-post/$', createPost)
]