from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import Product


def bag_contents(request):

    bag_items = []
    total = 999
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Use code here to also calculate premium membership discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count
    }

    return context
