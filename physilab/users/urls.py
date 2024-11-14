from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
]
