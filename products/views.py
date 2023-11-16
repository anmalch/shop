from django.shortcuts import render


def index(request):
    context = {
        'title': 'FashionShop'

    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'FashionShop - Catalog',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'image':'vendor/img/products/Adidas-hoodie.png', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'image': 'vendor/img/products/Blue-jacket-The-North-Face.png', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'image' : 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'price': '3 390,00'},
            {'name': 'Черный рюкзак Nike Heritage', 'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png', 'description': 'Плотная ткань. Легкий материал.', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'image': 'vendor/img/products/Black-Dr-Martens-shoes.png', 'description': 'Гладкий кожаный верх. Натуральный материал.', 'price': '13 590,00'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'price': '2 890,00'},
        ]
    }
    return render(request, 'products/products.html', context)
