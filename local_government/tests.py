from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import CouncilDecision


class CouncilDecisionTests(TestCase):
    # Створюємо приклади рішень для тестів списку та агрегації.
    def setUp(self):
        CouncilDecision.objects.create(
            council_name='Kyiv Council',
            title='Road repairs 2026',
            category='infrastructure',
            status=CouncilDecision.Status.APPROVED,
            budget_amount='1000000.00',
            decision_date=date(2026, 3, 10),
        )
        CouncilDecision.objects.create(
            council_name='Kyiv Council',
            title='School meals funding',
            category='education',
            status=CouncilDecision.Status.PROPOSED,
            budget_amount='350000.00',
            decision_date=date(2026, 3, 12),
        )

    # API списку має повертати всі створені записи.
    def test_list_returns_data(self):
        response = self.client.get(reverse('lg-decisions-list'))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['count'], 2)
        self.assertEqual(payload['limit'], 50)
        self.assertEqual(payload['offset'], 0)
        self.assertEqual(len(payload['results']), 2)

    # Перевірка валідації limit/offset.
    def test_list_invalid_limit(self):
        response = self.client.get(reverse('lg-decisions-list'), {'limit': 'bad'})
        self.assertEqual(response.status_code, 400)

    # Перевіряємо дефолтну агрегацію за назвою ради.
    def test_aggregate_default(self):
        response = self.client.get(reverse('lg-decisions-aggregate'))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['group_by'], 'council_name')
        self.assertEqual(len(payload['results']), 1)
        self.assertEqual(str(payload['results'][0]['total_budget']), '1350000')
        self.assertEqual(payload['results'][0]['total_decisions'], 2)

    # Невірне поле групування має дати 400.
    def test_aggregate_invalid_group(self):
        response = self.client.get(reverse('lg-decisions-aggregate'), {'group_by': 'invalid'})
        self.assertEqual(response.status_code, 400)
