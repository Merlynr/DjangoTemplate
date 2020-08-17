from django.contrib import admin

# Register your models here.

from django.contrib import admin
from polls import models

admin.site.register(models.Question)
admin.site.register(models.Choice)