import django_filters

from .models import *


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model=Task
        fields =['title','completetask','tasktype','created']
