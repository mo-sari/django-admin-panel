from django.contrib import admin
from .models import Course, Lecture


class InlineLecture(admin.StackedInline):
    # instead of StackedInline we could have
    # TabularInline
    model = Lecture
    # max_num = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [InlineLecture]
    prepopulated_fields = {
        'slug': ('course_title',)
    }


class LectureAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('lecture_name', )
    }
    # it works while adding a single Lecture
    # but while adding Lectures along with
    # a course, it won't


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Course, CourseAdmin)
