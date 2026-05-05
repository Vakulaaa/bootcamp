from django.db import models


class DataPoint(models.Model):
    # Джерело, звідки прийшли дані (наприклад, API/CSV).
    source = models.CharField(max_length=120)
    # Логічна категорія даних для подальшого групування.
    category = models.CharField(max_length=120)
    # Числове значення для агрегації; Decimal потрібен для точної математики.
    value = models.DecimalField(max_digits=12, decimal_places=2)
    # Дата створення запису для історії.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Нові записи показуємо першими.
        ordering = ['-created_at']

    def __str__(self):
        # Зручний короткий підпис у Django admin.
        return f"{self.source}:{self.category}={self.value}"
