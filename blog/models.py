from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=255)
    categories = models.ManyToManyField('Category', related_name='posts')

    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)

    body = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created_on = timezone.now()
        self.last_modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)