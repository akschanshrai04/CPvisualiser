from django.contrib import admin
from django.urls import include , path

urlpatterns = [
    # path("cpmain/", include("cpmain.urls")),
    path("" , include("cpmain.urls")),
    path("admin/", admin.site.urls),
]

