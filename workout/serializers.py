from workout.models import Workout, Exercise, SetOfReps
from rest_framework import serializers


class SetOfRepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetOfReps
        fields = ['order', 'info', 'nb_reps']


class ExerciseSerializer(serializers.ModelSerializer):
    sets_of_reps = SetOfRepsSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ['order', 'name', 'sets_of_reps']


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['name', 'rest_time', "exercises"]
