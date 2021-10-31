from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Superhero






# Create your views here.



def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context) 

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        print("Hit with post")
        # save the form contents as new database object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def delete(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    single_hero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))

def update(request, hero_id):
    updated_hero = Superhero.objects.get(pk=hero_id)
    form = EditSuperhero(request.POST or None, instance = updated_hero)
    if form.is_valid():
        form.save
    context = {
        'form':form,
        'updated_hero': updated_hero
    }
    return render(request, 'superheroes/update.html')
