from django.contrib import admin

from base.models import CategoryCourse, Course, MyUser, Review, Faq, News, CourseSchedule


admin.site.register(CategoryCourse)
admin.site.register(Course)
admin.site.register(MyUser)
admin.site.register(Review)
admin.site.register(Faq)
admin.site.register(News)
admin.site.register(CourseSchedule)