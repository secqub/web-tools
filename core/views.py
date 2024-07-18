from django.shortcuts import render
from .utils import software


# Create your views here.
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
