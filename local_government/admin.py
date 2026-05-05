from django.contrib import admin

from .models import CouncilDecision


@admin.register(CouncilDecision)
class CouncilDecisionAdmin(admin.ModelAdmin):
    # Налаштування відображення рішень рад у Django admin.
    list_display = ('id', 'council_name', 'title', 'category', 'status', 'budget_amount', 'decision_date')
    list_filter = ('council_name', 'category', 'status', 'decision_date')
    search_fields = ('council_name', 'title', 'category')
