from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('blog/<int:pk>', views.single, name='singleblog'),
    path('logout', views.logout, name='logout'),
]
