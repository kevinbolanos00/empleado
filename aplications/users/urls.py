
from django.urls import path
from . import views
app_name = "users_app"
#from aplications.home.views import IndexView

urlpatterns = [
    #path('home/', views.IndexView, name='home'),
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    
]
 