from django.shortcuts import get_object_or_404
from tours.models import Tour


def bag_contents(request):

    bag_items = []
    total = 0
    tour_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        tour = get_object_or_404(Tour, pk=item_id)
        total += quantity * tour.price
        tour_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'tour': tour,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'tour_count': tour_count,
        'grand_total': grand_total,
    }

    return context
