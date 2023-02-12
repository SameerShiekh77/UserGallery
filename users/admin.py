from django.contrib import admin
from users.models import User
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone_number','country', 'is_active',)
    search_fields = ('username', 'email','country','phone_number')
    list_per_page = 50

admin.site.register(User, UserAdmin)