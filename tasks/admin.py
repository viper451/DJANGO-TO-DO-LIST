from django.contrib import admin
from django.db.models.fields.related_descriptors import create_reverse_many_to_one_manager

# Register your models here.

from .models import *

admin.site.register(Task)

