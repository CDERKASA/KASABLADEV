from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = "kasaapp"

urlpatterns = [
    path('home', views.home, name='home'),
    path('overview', views.overview, name='overview'),
    path('characterization', views.characterization, name='characterization'),
    path('riskeval', views.riskeval, name='riskeval'),
    path('summary', views.summary, name='summary'),
    path('search-bla', csrf_exempt(views.search), name='search'),
    path('data/<int:bla>', views.show_data, name="show_data"),
]
