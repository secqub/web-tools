from django.shortcuts import render
from .api import DorksSearch


# Create your views here.
def index(request):
    return render(request, 'partials/searchmap_page.html')


def search(request):
    ds = DorksSearch()
    text = request.GET.get('searchmap', '')

    context = {
        'title': text,
        'result': ds.search_api(text)
    }

    return render(request, 'partials/searchmap_result_box.html', context=context)
