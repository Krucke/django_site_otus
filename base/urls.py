from django.urls import path

from base.views import Home, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView,\
    CourseDeleteView, AboutView, CategoryCourseCreateView


urlpatterns = [
    path('', Home.as_view()),
    path('course/list', CourseListView.as_view(), name='course-list'),
    path('course/detail/<slug:slug>', CourseDetailView.as_view(), name='course-detail'),
    path('course/create', CourseCreateView.as_view(), name='course-create'),
    path('course/update/<slug:slug>', CourseUpdateView.as_view(), name='course-update'),
    path('course/delete/<slug:slug>', CourseDeleteView.as_view(), name='course-delete'),
    path('about', AboutView.as_view(), name='about'),
    path('category/create', CategoryCourseCreateView.as_view(), name='category-create')
]