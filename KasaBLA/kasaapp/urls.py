from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('overview', views.overview, name='overview'),
    path('characterization', views.characterization, name='characterization'),
    path('riskevaluation', views.riskevaluation, name='riskevaluation'),
    path('riskeval', views.riskeval, name='riskeval'),
    path('summary', views.summary, name='summary'),

]
