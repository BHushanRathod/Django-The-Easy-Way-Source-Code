from django.contrib import admin

from myapp.models import Flower, Tag

admin.site.register(Flower)
admin.site.register(Tag)
