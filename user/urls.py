from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *

router = SimpleRouter()
router.register(r'intern', InternView, basename='user')
router.register(r'agent', AgentView, basename='agent')

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login')
]

urlpatterns += router.urls
