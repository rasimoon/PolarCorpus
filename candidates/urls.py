from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='default'),

    path('home/', views.home, name='home'),

    path('home/left', views.leftcandidates, name='leftcandidates'),
    path('home/right', views.rightcandidates, name='rightcandidates'),

    path('home/left/candidate', views.chosen_candidate_left, name='chosen_candidate_left'),
    path('home/right/candidate', views.chosen_candidate_right, name='chosen_candidate_right'),

    path("home/left/candidate/rating", views.submit_rating, name="submit_rating"),
    path("home/right/candidate/rating", views.submit_rating, name="submit_rating"),

    path("home/left/candidate/polarization", views.submit_polarization, name="submit_polarization"),
    path("home/right/candidate/polarization", views.submit_polarization, name="submit_polarization"),

    path("home/left/candidate/comment", views.submit_comment, name="submit_comment"),
    path("home/right/candidate/comment", views.submit_comment, name="submit_comment"), ]