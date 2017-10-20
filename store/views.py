from django.shortcuts import render, get_object_or_404
from store.models import Item, Category




def index(request, category_slug=None):
    categories = Category.objects.filter(is_visible=True)
    category = None
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug, is_visible=True)
    items = Item.objects.all()
    return render(request, 'pages/index.html', {'categories': categories, 'items': items, 'category': category})




def item(request, item_id):
    categories = Category.objects.filter(is_visible=True)
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'pages/item.html', {'categories': categories, 'item': item})




def checkout(request):
    categories = Category.objects.filter(is_visible=True)
    return render(request, 'pages/checkout.html', {'categories': categories})
