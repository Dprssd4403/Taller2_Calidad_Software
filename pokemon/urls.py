from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('cargar/', views.pokemon_sync_api, name='pokemon_sync_api'),
    path('crear/', views.pokemon_create, name='pokemon_create'),
    path('<int:pk>/', views.pokemon_detail, name='pokemon_detail'),
    path('<int:pk>/editar/', views.pokemon_update, name='pokemon_update'),
    path('<int:pk>/eliminar/', views.pokemon_delete, name='pokemon_delete'),
]
