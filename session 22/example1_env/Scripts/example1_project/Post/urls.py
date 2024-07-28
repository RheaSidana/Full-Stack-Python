from django.urls import path
from .views import *

urlpatterns = [
    path("my-post-tv/", MyPostTV.as_view(), name="my-post-tv"),
    path("my-post-dv/<int:id>", MyPostDV.as_view(), name="my-post-dv"),
    path("my-post-cv/", MyPostCV.as_view(), name="my-post-cv"),
    path("create-post-success-tv/", CreatePostTV.as_view(), name="create-post-success-tv"),
    path("my-post-lv/", MyPostsLV.as_view(), name="my-post-lv"),
    path("my-post-uv/<int:id>", MyPostUV.as_view(), name="my-post-uv"),
    path("my-post-dlv/<int:id>", MyPostDLV.as_view(), name="my-post-dlv"),
]
