from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tools/', views.ToolsView.as_view(), name='tools'),
    path('tools-search/', views.ToolsSearchView.as_view(), name='search'),
    path('tools/searchmap/', include('searchmap.urls', namespace='searchmap')),
]
