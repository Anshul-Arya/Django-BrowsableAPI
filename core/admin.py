from django.contrib import admin
from .models import Game
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Game)
class ViewAdmin(ImportExportModelAdmin):
    pass