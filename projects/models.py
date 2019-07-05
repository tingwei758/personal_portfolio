from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    group = models.BooleanField(default=False)
    image = models.FilePathField(path=settings.BASE_DIR + '/projects/static/img/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # On save, change image path to relative path
        self.image = self.image.replace(settings.BASE_DIR + '/projects/static/', '')
        return super(Project, self).save(*args, **kwargs)