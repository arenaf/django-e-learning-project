from django.contrib import admin
from .models import Subject, File


class SubjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class FileAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("description", "file")


admin.site.register(Subject, SubjectAdmin)
admin.site.register(File, FileAdmin)
