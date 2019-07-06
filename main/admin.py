from django.contrib import admin
from .models import Code
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.
class CodeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Code', {'fields' : ['body']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Code, CodeAdmin)