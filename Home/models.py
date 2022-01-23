from django.db import models
from django.contrib.auth.models import User


from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField( max_length=50)
    body = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
