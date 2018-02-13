from django.conf.urls import url
from api import views


urlpatterns = [
    url(r"^posts/$", views.posts_list, name="posts_list"),
    url(r"^posts/(?P<posts_id>\d+)$", views.posts_detail, name="posts_detail"),
]
