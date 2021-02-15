from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_querySet(self):
        return super(PublishedManager, self).get_querySet().filter(status='published')
        
class Post(models.Model):

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to="img/", default="")

    body= models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args = [self.publish.year,self.publish.month,self.publish.day, self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Contact(models.Model):
    Name = models.CharField(max_length = 250)
    Email_Address = models.EmailField(max_length = 250)
    Phone_Number = models.CharField(max_length = 30)
    message = models.CharField(max_length = 500)


# Create your models here.
