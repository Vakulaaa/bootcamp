from django.db.models import Count, Sum, Value
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import CouncilDecision


@require_GET
def decisions_list(request):
    # Повертаємо базовий список рішень для перегляду без агрегації.
    # Додаємо просту пагінацію через limit/offset, щоб не віддавати весь обсяг одразу.
    try:
        limit = int(request.GET.get('limit', 50))
        offset = int(request.GET.get('offset', 0))
    except ValueError:
        return JsonResponse({'error': 'limit and offset must be integers'}, status=400)

    if limit < 1 or limit > 500:
        return JsonResponse({'error': 'limit must be between 1 and 500'}, status=400)
    if offset < 0:
        return JsonResponse({'error': 'offset must be >= 0'}, status=400)

    queryset = CouncilDecision.objects.values(
        'id',
        'council_name',
        'title',
        'category',
        'status',
        'budget_amount',
        'decision_date',
    )

    total = queryset.count()
    decisions = list(queryset[offset:offset + limit])
    return JsonResponse({'count': total, 'limit': limit, 'offset': offset, 'results': decisions})


@require_GET
def decisions_aggregate(request):
    # За замовчуванням групуємо по назві ради.
    group_by = request.GET.get('group_by', 'council_name')

    # Дозволяємо тільки безпечний і очікуваний набір полів.
    if group_by not in {'council_name', 'category', 'status'}:
        return JsonResponse(
            {'error': "group_by must be one of: council_name, category, status"},
            status=400,
        )

    # Рахуємо кількість рішень і суму бюджету в кожній групі.
    rows = (
        CouncilDecision.objects.values(group_by)
        .annotate(
            total_decisions=Count('id'),
            total_budget=Coalesce(Sum('budget_amount'), Value(0)),
        )
        .order_by(group_by)
    )

    return JsonResponse({'group_by': group_by, 'results': list(rows)})
