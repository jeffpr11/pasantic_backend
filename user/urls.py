from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()
router.register(r'', InternView, basename='user')

urlpatterns = router.urls
