from django.db.models import Avg, Count, Max, Min, Sum, Value
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import DataPoint


@require_GET
def aggregate_data(request):
    # Параметр визначає, по якому полю робимо зведення.
    group_by = request.GET.get('group_by', 'category')

    # Явна валідація параметра, щоб уникнути помилок і неочікуваних полів.
    if group_by not in {'category', 'source'}:
        return JsonResponse(
            {'error': "group_by must be either 'category' or 'source'"},
            status=400,
        )

    # Формуємо агреговану статистику для кожної групи.
    # Coalesce дає 0, якщо сума/середнє ще відсутні.
    rows = (
        DataPoint.objects.values(group_by)
        .annotate(
            total=Coalesce(Sum('value'), Value(0)),
            average=Coalesce(Avg('value'), Value(0)),
            minimum=Min('value'),
            maximum=Max('value'),
            records=Count('id'),
        )
        .order_by(group_by)
    )

    # Повертаємо результат у JSON для API-клієнтів.
    return JsonResponse({'group_by': group_by, 'results': list(rows)})
