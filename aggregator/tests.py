from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import DataPoint


class AggregateDataViewTests(TestCase):
    # Готуємо тестові дані для перевірки агрегації.
    def setUp(self):
        DataPoint.objects.create(source='api', category='sales', value=Decimal('10.00'))
        DataPoint.objects.create(source='api', category='sales', value=Decimal('20.00'))
        DataPoint.objects.create(source='csv', category='marketing', value=Decimal('5.00'))

    # Перевіряємо успішну агрегацію за замовчуванням (по category).
    def test_aggregate_by_category(self):
        response = self.client.get(reverse('aggregate-data'))
        self.assertEqual(response.status_code, 200)

        payload = response.json()
        self.assertEqual(payload['group_by'], 'category')
        self.assertEqual(len(payload['results']), 2)

        by_category = {row['category']: row for row in payload['results']}
        self.assertEqual(str(by_category['sales']['total']), '30')
        self.assertEqual(str(by_category['sales']['minimum']), '10')
        self.assertEqual(str(by_category['sales']['maximum']), '20')
        self.assertEqual(by_category['sales']['records'], 2)

    # Перевіряємо, що для невалідного group_by API повертає 400.
    def test_invalid_group_by(self):
        response = self.client.get(reverse('aggregate-data'), {'group_by': 'unknown'})
        self.assertEqual(response.status_code, 400)
