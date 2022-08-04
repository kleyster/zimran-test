from django.contrib import admin
from .models import News,NewsImages


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsImages)
class NewsImageAdmin(admin.ModelAdmin):
    pass