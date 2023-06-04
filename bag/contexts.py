

def bag_contents(request):

    bag_items = []
    total = 0
    tour_count = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'tour_count': tour_count,
        'grand_total': grand_total,
    }

    return context
