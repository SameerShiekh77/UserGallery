from django.contrib import admin
from gallery.models import Photo
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PhotoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title','image','created_at')
    search_fields = ('title',)
    list_per_page = 30

admin.site.register(Photo,PhotoAdmin)