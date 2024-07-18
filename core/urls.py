from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('tools/', views.tools, name='tools'),
    path('tools/searchmap/', include('searchmap.urls', namespace='searchmap')),

]
