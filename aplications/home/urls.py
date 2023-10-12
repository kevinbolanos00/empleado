from os import name
from django.urls import path, include
from . import views
#from aplications.home.views import IndexView
app_name="home_app"
urlpatterns = [
    #path('home/', views.IndexView, name='home'),
    path('home/',
          views.IndexView.as_view(),
          name='home'
        ),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'), 
    path('resume-foundation/', views.ResumenFoundationView.as_view(), name='resume_foundation'), 
]
 