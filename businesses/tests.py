from datetime import date, timedelta

from django.test import TestCase

from businesses.models import LocalBusiness


class IsCurrentlyActiveTests(TestCase):
    """LocalBusiness.is_currently_active property — unsaved instance'larla test edilir (DB yok)."""

    def _business(self, is_published, end_date):
        return LocalBusiness(is_published=is_published, end_date=end_date)

    def test_active_when_published_and_future_end_date(self):
        b = self._business(True, date.today() + timedelta(days=30))
        self.assertTrue(b.is_currently_active)

    def test_active_when_end_date_is_today(self):
        b = self._business(True, date.today())
        self.assertTrue(b.is_currently_active)

    def test_inactive_when_not_published(self):
        b = self._business(False, date.today() + timedelta(days=30))
        self.assertFalse(b.is_currently_active)

    def test_inactive_when_end_date_yesterday(self):
        b = self._business(True, date.today() - timedelta(days=1))
        self.assertFalse(b.is_currently_active)

    def test_inactive_when_no_end_date(self):
        b = self._business(True, None)
        self.assertFalse(b.is_currently_active)

    def test_inactive_when_both_unpublished_and_expired(self):
        b = self._business(False, date.today() - timedelta(days=10))
        self.assertFalse(b.is_currently_active)
