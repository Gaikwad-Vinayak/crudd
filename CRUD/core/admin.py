from django.contrib import admin
from .models import librarymanagement_module
# Register your models here.
@admin.register(librarymanagement_module)
class admina(admin.ModelAdmin):
    list_display=['title','category','formats','location','total_pages']