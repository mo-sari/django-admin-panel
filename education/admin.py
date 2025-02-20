from django.contrib import admin
from .models import Course, Lecture


class InlineLecture(admin.StackedInline):
    model = Lecture


class CourseAdmin(admin.ModelAdmin):
    inlines = [InlineLecture]
    list_display = ['course_title',
                    'course_description',
                    'course_heading']
    prepopulated_fields = {
        'slug': ('course_title',)
    }
    fieldsets = (
        ('First Section', {
            'fields': ('course_title', ),
            'description': 'The main section'
        }),
        ('section section', {
            'fields': ('slug', )
        }),
    )

    def course_heading(self, obj):
        return obj.course_title + " - " + obj.course_description


class LectureAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('lecture_name', )
    }


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Course, CourseAdmin)
