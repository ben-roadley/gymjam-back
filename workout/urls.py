from django.urls import include, path
from rest_framework import routers

from workout import views

router = routers.DefaultRouter()
router.register(r'workouts', views.WorkoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]