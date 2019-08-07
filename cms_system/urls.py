from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('courses', views.CourseViewSet)
router.register('degrees', views.DegreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
