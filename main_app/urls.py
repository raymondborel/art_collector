from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    path('artworks/', views.ArtworkList.as_view(), name="artwork_list"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/update',views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete',views.ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/artworks/new/', views.ArtworkCreate.as_view(), name="artwork_create"),
    path('collections/<int:pk>/artworks/<int:artwork_pk>/', views.CollectionArtworkAssoc.as_view(), name="collection_artwork_assoc"),
    ]
