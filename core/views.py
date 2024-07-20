from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .utils import software


# Create your views here.
@cache_page(60 * 2)
def index(request):
    return render(request, 'index.html')


def tools(request):
    context = {
        'bar': software
    }

    return render(request, 'tools.html', context)


def tools_search(request):
    text = request.GET.get('aside-search')

    bar = {i: software[i] for i in software if text in i.lower()}
    context = {
        'bar': bar,
    }

    return render(request, 'partials/aside.html', context)
