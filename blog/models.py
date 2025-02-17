from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', "Published")
    )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 default=1)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name='blog_posts')
    content = models.TextField(null=True)
    status = models.CharField(max_length=30,
                              choices=options,
                              default='draft')

    def __str__(self):
        return self.title
