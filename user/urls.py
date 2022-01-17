from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *

router = SimpleRouter()
router.register(r'intern', InternView, basename='user')
router.register(r'agent', AgentView, basename='agent')

urlpatterns = router.urls
