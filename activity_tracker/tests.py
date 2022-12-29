from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Activity, Athlete

class ActivityModelTests(TestCase):

    def setUp(self):
        Athlete.objects.create(username='TestUser')

    def test_was_published_recently_with_future_date(self):
        """
        was_published_recently() return False for questions whose start_date are
        in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        athlete = Athlete.objects.get(username='TestUser')
        futureActivity = Activity(athlete=athlete, start_date=time)

        self.assertFalse(futureActivity.was_published_recently())

    def test_was_published_recently_with_old_date(self):
        """
        was_published_recently() return False for questions whose start_date are
        older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        athlete = Athlete.objects.get(username='TestUser')
        pastActivity = Activity(athlete=athlete, start_date=time)

        self.assertFalse(pastActivity.was_published_recently())

    def test_was_published_recently_with_recent_date(self):
        """
        was_published_recently() return True for questions whose start_date are
        within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        athlete = Athlete.objects.get(username='TestUser')
        recentActivity = Activity(athlete=athlete, start_date=time)

        self.assertTrue(recentActivity.was_published_recently())