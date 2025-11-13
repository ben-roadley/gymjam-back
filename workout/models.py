from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Workout(models.Model):
    name = models.CharField(max_length=200, help_text="Provide a name for the workout which describes it concisely and efficiently.")
    rest_time = models.SmallIntegerField(default=90, validators=[MinValueValidator(0), MaxValueValidator(300)], help_text="In seconds, how much time to rest between sets.")
    
    def __str__(self):
        return f"{self.name}"


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name="exercises", on_delete=models.CASCADE)
    order = models.SmallIntegerField(help_text="The order in sequence of exercises for specified workout.")
    name = models.CharField(max_length=200, help_text="Provide a name for the exercise which is recognizable by you and others.")
    
    class Meta:
        ordering = ["workout", "order"]
        constraints = [
            models.UniqueConstraint(
                fields=["workout", "order"],
                name="unique_order_for_workout"
            )
        ]
    
    def __str__(self):
        return f"{self.workout.name} - {self.name}"


class SetOfReps(models.Model):
    exercise = models.ForeignKey(Exercise, related_name="sets_of_reps", on_delete=models.CASCADE)
    order = models.SmallIntegerField(help_text="The order in sequence of sets for specified exercise.")
    info = models.CharField(max_length=200, help_text="Useful instructions, like weight, intensity, how-to, etc")
    nb_reps = models.SmallIntegerField(help_text="The number of reps to aim for in this set.")
    
    class Meta:
        ordering = ["exercise", "order"]
        verbose_name_plural = "Sets of reps"
        constraints = [
            models.UniqueConstraint(
                fields=["exercise", "order"],
                name="unique_order_for_exercise"
            )
        ]

    def __str__(self):
        return f"{self.exercise.workout.name} - {self.exercise.name} - Set #{self.order}"