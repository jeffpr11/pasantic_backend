from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *

router = SimpleRouter()
router.register(r'enterprise', EnterpriseView, basename='enterprise')
router.register(r'review', ReviewView, basename='review')

urlpatterns = router.urls