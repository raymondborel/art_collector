from typing import Any, Dict
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Artist, Artwork, Collection
from django.urls import reverse


class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context


class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'image', 'bio']
    template_name = "artist_create.html"
    success_url = '/artists/'

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Artist.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["artists"] = Artist.objects.all()
            context["header"] = "Trending Artists"
        return context
    
class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'image', 'bio']
    template_name = "artist_update.html"
    success_url = "/artists/"
    
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})
    
class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"
    


class ArtworkList(TemplateView):
    template_name = "artwork_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artworks"] = Artwork.objects.all() 
        return context
    
class ArtworkCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        artist = Artist.objects.get(pk=pk)
        Artwork.objects.create(name=name, image=image, artist=artist)
        return redirect('artist_detail', pk=pk)
    
class CollectionArtworkAssoc(View):

    def get(self, request, pk, artwork_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the Collection by the id and
            # remove from the join table the given song_id
            Collection.objects.get(pk=pk).artworks.remove(artwork_pk)
        if assoc == "add":
            # get the Collection by the id and
            # add to the join table the given artwork_id
            Collection.objects.get(pk=pk).artworks.add(artwork_pk)
        return redirect('home')

    
