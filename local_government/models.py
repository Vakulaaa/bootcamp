from django.db import models


class CouncilDecision(models.Model):
    # Довідник можливих статусів рішення.
    class Status(models.TextChoices):
        PROPOSED = 'proposed', 'Proposed'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    # Назва місцевої ради, що ухвалила або розглядає рішення.
    council_name = models.CharField(max_length=180)
    # Коротка назва/тема рішення.
    title = models.CharField(max_length=255)
    # Категорія: освіта, інфраструктура, медицина тощо.
    category = models.CharField(max_length=120)
    # Поточний статус проходження рішення.
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROPOSED)
    # Бюджет, пов'язаний із рішенням.
    budget_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # Дата ухвалення/розгляду рішення.
    decision_date = models.DateField()
    # Технічне поле для аудиту створення запису.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Останні рішення показуємо першими.
        ordering = ['-decision_date', '-created_at']

    def __str__(self):
        # Зручний текст у списках адмінки та shell.
        return f"{self.council_name}: {self.title}"
