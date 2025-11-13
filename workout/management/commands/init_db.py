from django.core.management.base import BaseCommand, CommandError
from workout.models import Workout, Exercise, SetOfReps


class Command(BaseCommand):
    help = "Initializes the Workout database."

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        # raise CommandError('Poll "%s" does not exist' % poll_id)

        Workout.objects.all().delete()

        Workout.objects.create(name="Ben's MTB Workout")
        w = Workout.objects.first()

        Exercise.objects.create(workout=w, order=1, name="Easy Dips")
        Exercise.objects.create(workout=w, order=2, name="Push ups high hands")
        Exercise.objects.create(workout=w, order=3, name="MTB Push-ups with knees bent")
        Exercise.objects.create(workout=w, order=4, name="Bicep curls")
        Exercise.objects.create(workout=w, order=5, name="Rows")
        Exercise.objects.create(workout=w, order=6, name="Squats")
        Exercise.objects.create(workout=w, order=7, name="Deadlifts")
        Exercise.objects.create(workout=w, order=8, name="Abs")

        e = Exercise.objects.all()

        SetOfReps.objects.create(exercise=e[0], order=1, info="Coffee table.", nb_reps="12")
        SetOfReps.objects.create(exercise=e[0], order=2, info="Coffee table.", nb_reps="12")
        SetOfReps.objects.create(exercise=e[0], order=3, info="Coffee table.", nb_reps="12")

        SetOfReps.objects.create(exercise=e[1], order=1, info="Sofa.", nb_reps="8")
        SetOfReps.objects.create(exercise=e[1], order=2, info="Sofa.", nb_reps="8")
        SetOfReps.objects.create(exercise=e[1], order=3, info="Sofa.", nb_reps="8")

        SetOfReps.objects.create(exercise=e[2], order=1, info="Hands the width of handlebar.", nb_reps="8")
        SetOfReps.objects.create(exercise=e[2], order=2, info="Hands the width of handlebar.", nb_reps="8")
        SetOfReps.objects.create(exercise=e[2], order=3, info="Hands the width of handlebar.", nb_reps="8")

        SetOfReps.objects.create(exercise=e[3], order=1, info="25kg", nb_reps="8")
        SetOfReps.objects.create(exercise=e[3], order=2, info="25kg", nb_reps="8")
        SetOfReps.objects.create(exercise=e[3], order=3, info="25kg", nb_reps="8")

        SetOfReps.objects.create(exercise=e[4], order=1, info="25+20kg", nb_reps="8")
        SetOfReps.objects.create(exercise=e[4], order=2, info="25+20kg", nb_reps="8")
        SetOfReps.objects.create(exercise=e[4], order=3, info="25+20kg", nb_reps="8")

        SetOfReps.objects.create(exercise=e[5], order=1, info="25kg", nb_reps="12")
        SetOfReps.objects.create(exercise=e[5], order=2, info="25kg", nb_reps="12")
        SetOfReps.objects.create(exercise=e[5], order=3, info="25kg", nb_reps="12")

        SetOfReps.objects.create(exercise=e[6], order=1, info="25kg", nb_reps="12")
        SetOfReps.objects.create(exercise=e[6], order=2, info="25kg", nb_reps="12")
        SetOfReps.objects.create(exercise=e[6], order=3, info="25kg", nb_reps="12")

        SetOfReps.objects.create(exercise=e[7], order=1, info="Crunches, no weights.", nb_reps="35")
        SetOfReps.objects.create(exercise=e[7], order=2, info="Crunches, no weights.", nb_reps="35")
        SetOfReps.objects.create(exercise=e[7], order=3, info="Crunches, no weights.", nb_reps="35")

        self.stdout.write(
            self.style.SUCCESS('Successfully initialized db.')
        )