from django.contrib import admin
from .models import Category, Courses, Lessons, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class CategorysAdmin(admin.ModelAdmin):
    list_display = ('pk',"name",)
    list_filter = ("id",)
    search_fields = ("name",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("id","name")


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    #Nhớ ghi đè Upload Form của Trường (vd: description) xài Rich Text Field

    class Meta:
        model = Courses
        fields = '__all__'

class CourseAdmin (admin.ModelAdmin):
    # list_display = ("id","name","description")
    readonly_fields = ['img']
    form=CourseForm
    def img(self, course):
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=course.image.name)
            )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


class LessonsAdmin (admin.ModelAdmin):
    list_display = ("id","name","course") #subject ==name
    list_filter = ["name"]
    search_fields = ['name', "course__name"]

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }
# Register your models here.

admin.site.register(Category,CategorysAdmin)
admin.site.register(Courses,CourseAdmin)
admin.site.register(Lessons,LessonsAdmin)
admin.site.register(Tag,TagAdmin)
