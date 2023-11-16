import os
import json

from django.shortcuts import render

#константа хранит информацию путя до папки products
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'FashionShop'

    }
    return render(request, 'products/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/products.json' ) #соединение двух путей
    context = {
        'title': 'FashionShop - Catalog',
        'products': json.load(open(file_path, encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
