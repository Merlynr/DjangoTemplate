# Register your models here.

from django.contrib import admin

from polls import models

# admin.site.register(models.Question)
# admin.site.register(models.Choice)
from polls.models import *

admin.site.register(Records)
admin.site.register([Question, Choice])
