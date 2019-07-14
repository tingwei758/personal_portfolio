from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.
class Project(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['url'], name='unique_url'),
        ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    group = models.BooleanField(default=False)
    image = models.ImageField(upload_to='projects/img/')
    # image = models.FilePathField(path=settings.BASE_DIR + '/projects/static/img/')
    url = models.SlugField(blank=True, editable=False)
    filename = models.CharField(max_length=100, default='project_detail.html')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # On save, change image path to relative path
        # self.image = self.image.replace(settings.BASE_DIR + '/projects/static/', '')
        self.url = self.s = slugify(self.title)
        return super(Project, self).save(*args, **kwargs)