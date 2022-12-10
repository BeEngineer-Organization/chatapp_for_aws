from django.urls import include, path  # include を追加
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")), # 追加
]