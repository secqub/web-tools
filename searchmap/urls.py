from django.urls import path
from . import views

app_name = 'searchmap'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
]
