from django.urls import path
from . import views

urlpatterns = [
        path ( "" , views.story_page , name ="story_page") ,
        path ( "save/", views.save_story , name ="save_story") ,
    ]

