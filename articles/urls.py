from django.urls import path
from . import views

app_name = "article"
urlpatterns = [
    path('', views.articlesList, name="list"),
    path('create', views.articleCreate, name="create"),
    path('<slug>', views.articlesDitail, name="detail"),
]
