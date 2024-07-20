from django.shortcuts import render
from django.views.generic import TemplateView

from .api import DorksSearch
from django.core.cache import cache


class IndexView(TemplateView):
    template_name = 'partials/searchmap_page.html'


class SearchView(TemplateView):
    template_name = 'partials/searchmap_result_box.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('searchmap')
        ds = DorksSearch()
        result = ds.search_api(query) if query else ''

        context['title'] = query
        context['result'] = result
        return context

