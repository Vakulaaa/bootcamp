from django.contrib import admin

from .models import DataPoint


@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    # Налаштування списку в Django admin для швидкого перегляду записів.
    list_display = ('id', 'source', 'category', 'value', 'created_at')
    search_fields = ('source', 'category')
    list_filter = ('source', 'category', 'created_at')
