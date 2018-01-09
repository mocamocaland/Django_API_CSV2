from django.conf.urls import url
from api import views


urlpatterns = [
    url(r"^post/$", views.posts_list, name="posts_list"),
]
