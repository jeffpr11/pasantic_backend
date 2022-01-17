from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import *

router = SimpleRouter()

router.register(r'internship', InternshipView, basename='internship')
router.register(r'postulation', PostulationView, basename='postulation')


urlpatterns = router.urls