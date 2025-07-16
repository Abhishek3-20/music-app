from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('artists/', views.artists, name='artists'),
    path('listen/', views.listen, name='listen'),
    path('playlists/', views.playlists, name='playlists'),
    path('search/', views.search, name='search'),
]