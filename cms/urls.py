from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include has app_name.urls
    path('', include('cms_system.urls')),
    path('api-auth', include('rest_framework.urls'))
]
