from django.urls import path
from .views import HomeView

app_name = 'home_page'

urlpatterns = [
    path('', HomeView.as_view(), name='Home-Page'),
]