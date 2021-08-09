from django.db.models.fields import DateField
from django.shortcuts import render
from . import models
# Create your views here.


def articlesList(request):
    articlces = models.Articles.objects.all().order_by('time')

    args = {'articles': articlces}
    return render(request, 'articles/articlesList.html', args)
