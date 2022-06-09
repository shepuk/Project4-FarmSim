from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 999
    product_count = 0

    # Use code here to also calculate premium membership discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count
    }

    return context
