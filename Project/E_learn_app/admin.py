from django.contrib import admin
from .models import Main, AllCourses,VideoLibrarys


class MainAdmin(admin.ModelAdmin):
    list_display = ['name']


class AllCourseAdmin(admin.ModelAdmin):
    list_display = ['name']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.

admin.site.register(Main, MainAdmin)
admin.site.register(AllCourses, AllCourseAdmin)
admin.site.register(VideoLibrarys,VideoAdmin)