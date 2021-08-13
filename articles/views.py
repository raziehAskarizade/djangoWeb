from django.db.models.fields import DateField
from django.shortcuts import redirect, render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def articlesList(request):
    articlces = models.Articles.objects.all().order_by('-time')

    args = {'articles': articlces}
    return render(request, 'articles/articlesList.html', args)


def articlesDitail(request, slug):
    textBody = models.Articles.objects.get(slug=slug)
    return render(request, 'articles/articleDetail.html', {'textBody': textBody})


@login_required(login_url="/accounts/login")
def articleCreate(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('article:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/articleCreate.html', {'form': form})
