from django.urls import path
from . import views


app_name = "project"

urlpatterns = [
    path("", views.main, name="main"),
    path("carrot/", views.carrot, name="carrot"),
    # path("cooluid/", views.cooluid, name="cooluid"),
    # path("youtube/", views.youtube, name="youtube"),
    # path("heyPlaz/", views.heyPlaz, name="heyPlaz"),
    # path("Heresy_Tracker/", views.Heresy_Tracker, name="Heresy_Tracker"),
    # path("ai_blog/", views.ai_blog, name="ai_blog"),
]