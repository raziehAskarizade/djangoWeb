from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def snipet(self):
        return '... ' + self.body[:50]