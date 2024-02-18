from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    #categories = Categories.object.all()
    
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        #'categories': categories
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Blanditiis magni recusandae maxime sit, maiores repudiandae praesentium! Rerum explicabo amet, autem nihil debitis nostrum eius unde libero? Blanditiis, eos? Inventore, facilis '
        
    }
    return render(request, 'main/about.html', context)