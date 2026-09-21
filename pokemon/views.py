from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Pokemon
from .forms import PokemonForm
from .services.pokemon_service import sync_pokemons_from_api

# L - List (Con Paginación)
def pokemon_list(request):
    pokemons_all = Pokemon.objects.all()
    paginator = Paginator(pokemons_all, 8)  # 8 tarjetas por página
    page_number = request.GET.get('page')
    pokemons = paginator.get_page(page_number)
    return render(request, 'pokemon/pokemon_list.html', {'pokemons': pokemons})

# C - Create
def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Pokémon creado exitosamente!')
            return redirect('pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'pokemon/pokemon_form.html', {'form': form, 'title': 'Crear Pokémon'})

# R - Read / Detail
def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'pokemon/pokemon_details.html', {'pokemon': pokemon})

# U - Update
def pokemon_update(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Pokémon actualizado correctamente!')
            return redirect('pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon/pokemon_form.html', {'form': form, 'title': 'Editar Pokémon'})

# D - Delete
def pokemon_delete(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        messages.success(request, 'Pokémon eliminado.')
        return redirect('pokemon_list')
    return render(request, 'pokemon/pokemon_confirm_delete.html', {'pokemon': pokemon})

# Cargar desde API
def pokemon_sync_api(request):
    if request.method == 'POST':
        count = sync_pokemons_from_api(limit=20)
        messages.success(request, f'Se cargaron {count} nuevos Pokémon desde la API.')
    return redirect('pokemon_list')