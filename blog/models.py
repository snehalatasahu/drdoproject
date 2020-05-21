from django.db import models
import datetime
from django.db.models.signals import pre_save
from drdoproject.utils import unique_slug_generator

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField()
    publish_date = models.DateField(auto_now='True')

    def __str__(self):
        return self.title

class RecruitmentPost(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField()
    publish_date = models.DateField(auto_now='True')

    def __str__(self):
        return self.title
    


class Picture(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pic = models.ImageField()
    
    def __str__(self):
        return str(self.post)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
pre_save.connect(slug_generator, sender=RecruitmentPost)