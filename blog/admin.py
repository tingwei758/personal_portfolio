from django.contrib import admin
from .models import Post, Category
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title/Categories', {'fields' : ['title', 'categories']}),
        ('Dates', {'fields' : ['created_on', 'last_modified']}),
        ('Content', {'fields' : ['body']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Category)