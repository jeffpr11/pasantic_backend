from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/organization/', include('organization.urls')),
    path('api/', include('internships.urls')),
]
