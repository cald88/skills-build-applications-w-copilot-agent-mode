from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop the entire database
        from django.db import connection
        client = connection.cursor().db_conn.client
        client.drop_database('octofit_db')

        # Recreate collections and test data
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]

        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-09-10')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-09-09')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-09-08')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-09-07')

        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Marvel')
        Workout.objects.create(name='Squats', description='Lower body strength', suggested_for='DC')

        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db dropped and repopulated with test data'))

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-09-10')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-09-09')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-09-08')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-09-07')

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Marvel')
        Workout.objects.create(name='Squats', description='Lower body strength', suggested_for='DC')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
