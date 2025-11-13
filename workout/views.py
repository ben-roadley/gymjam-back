from .models import Workout
from rest_framework import viewsets

from workout.serializers import WorkoutSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
