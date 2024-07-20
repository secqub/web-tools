from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from .utils import software


# Create your views here.
# @cache_page(60 * 10)
class IndexView(TemplateView):
    template_name = 'index.html'


class ToolsView(TemplateView):
    template_name = 'tools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bar'] = software
        return context


class ToolsSearchView(TemplateView):
    template_name = 'partials/aside.html'

    def get_context_data(self, **kwargs):
        text = self.request.GET.get('aside-search').lower()
        if text:
            bar = {i: software[i] for i in software if text in i.lower()}
        else:
            bar = software

        context = super().get_context_data(**kwargs)
        context['bar'] = bar
        return context
