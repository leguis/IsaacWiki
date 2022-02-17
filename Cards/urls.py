from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.list_view),
    path('<int:card_id>/', views.card_view, name='card')
]