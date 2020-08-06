from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.index, name="register"),
    path('login/', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('confirm/', views.confirm, name="confirm"),
]
