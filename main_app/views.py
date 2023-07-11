from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Artist
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class Artist:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'image', 'bio']
    template_name = "artist_create.html"
    success_url = '/artists/'

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["artists"] = Artist.objects.filter(name__icontains=name)
        else:
            context["artists"] = Artist.objects.all()
        return context
    

class Artwork:
    def __init__(self, name, image, artist, materials):
        self.name = name
        self.image = image
        self.artist = artist
        self.materials = materials

class ArtworkList(TemplateView):
    template_name = "artwork_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artworks"] = artworks
        return context
    
artworks = [
    Artwork("So Much Fun", "https://d7hftxdivxxvm.cloudfront.net/?height=800&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FLA0gRTplt6EuB_IeDXOJdA%2Fnormalized.jpg&width=800", "Takashi Murakami", "Offset print with silver and high gloss varnishing"),
    Artwork("So Much Fun", "https://d7hftxdivxxvm.cloudfront.net/?height=800&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FLA0gRTplt6EuB_IeDXOJdA%2Fnormalized.jpg&width=800", "Takashi Murakami", "Offset print with silver and high gloss varnishing"),
    Artwork("So Much Fun", "https://d7hftxdivxxvm.cloudfront.net/?height=800&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FLA0gRTplt6EuB_IeDXOJdA%2Fnormalized.jpg&width=800", "Takashi Murakami", "Offset print with silver and high gloss varnishing"),
    Artwork("So Much Fun", "https://d7hftxdivxxvm.cloudfront.net/?height=800&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FLA0gRTplt6EuB_IeDXOJdA%2Fnormalized.jpg&width=800", "Takashi Murakami", "Offset print with silver and high gloss varnishing"),
]



# artists = [
#   Artist("Salvador Dali", "https://mgm-website-production.oss-cn-hongkong.aliyuncs.com/uploads/2018/01/salvador-dali-1024.jpg",
#           "Salvador Domingo Felipe Jacinto Dalí i Domènech, Marquess of Dalí of Púbol, known as Salvador Dalíwas a Spanish surrealist artist renowned for his technical skill, precise draftsmanship, and the striking and bizarre images in his work."),
#   Artist("Takashi Murakami",
#           "https://malvernschool.com/wp-content/uploads/2019/05/Artist-of-the-Month.jpg", "Takashi Murakami (村上 隆, Murakami Takashi, born February 1, 1962) is a Japanese contemporary artist."),
#   Artist("Joji", "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df",
#           "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
#   Artist("Metallica",
#           "https://i.scdn.co/image/ab67706c0000da84eb6bb372a485d26fd32d1922", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
#   Artist("Bad Bunny",
#           "https://www.clashmusic.com/sites/default/files/sty…e/Bad-Bunny-YHLQMDLG-Album-2020.jpg?itok=tbZNj82L", "Benito Antonio Martínez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
#   Artist("Kaskade",
#           "https://i1.sndcdn.com/artworks-sNjd3toBZYCG-0-t500x500.jpg", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
# ]
