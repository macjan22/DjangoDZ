import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

from recipes.settings import BASE_DIR


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template = 'home.html'
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter'),
    }
    context = {
        'pages': pages
    }
    return render(request, template, context)

def omlet(request):
    template = 'index.html'
    recipe = {'recipe': DATA['omlet']}
    if request.GET.get('count') is not None:
        c = request.GET.get('count')
        dict_ing = {}
        for ing, count in DATA['omlet'].items():
            dict_ing[ing] = round (float(count) * int(c),2)
        recipe = {'recipe': dict_ing}
    return render(request, template, recipe)


def pasta(request):
    template = 'index.html'
    recipe = {'recipe': DATA['pasta']}
    if request.GET.get('count') is not None:
        c = request.GET.get('count')
        dict_ing = {}
        for ing, count in DATA['pasta'].items():
            dict_ing[ing] = round(float(count) * int(c),2)
        recipe = {'recipe': dict_ing}
    return render(request, template, recipe)


def buter(request):
    template = 'index.html'
    recipe = {'recipe': DATA['buter']}
    if request.GET.get('count') is not None:
        c = request.GET.get('count')
        dict_ing = {}
        for ing, count in DATA['buter'].items():
            dict_ing[ing] = round(float(count) * int(c),2)
        recipe = {'recipe': dict_ing}
    return render(request, template, recipe)
