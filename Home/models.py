from django.db import models
from django.contrib.auth.models import User


from django.urls import reverse

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50)

    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=50)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField( max_length=50)
    body = models.TextField()
    Date_field = models.DateField(auto_now_add=True)
    categories = models.CharField(max_length=50, default="coding")




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
