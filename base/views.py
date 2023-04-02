from django.views.generic.base import TemplateView

from base.models import Course, CategoryCourse, MyUser

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from django.urls import reverse


class Home(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        courses = Course.objects.all().select_related('category')
        context['courses'] = courses
        return self.render_to_response(context)
    

class UserView(TemplateView):

    template_name = 'user_view.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        users = MyUser.objects.filter(is_superuser=False).prefetch_related('courses')
        context['users'] = users
        return self.render_to_response(context)
    

class CategoryCourseCreateView(CreateView):

    model = CategoryCourse
    fields = ('name', 'slug')
    template_name = 'category_create.html'
    

class CourseListView(ListView):

    model = Course
    template_name = 'course_list.html'

    def get_queryset(self):
        return Course.objects.all().select_related('category')


class CourseDetailView(DetailView):

    model = Course
    template_name = 'course_detail.html'


class CourseCreateView(CreateView):

    model = Course
    template_name = 'course_create.html'
    fields = ('name', 'slug', 'description', 'duration_days', 'category')


class CourseUpdateView(UpdateView):

    model = Course
    fields = ('name', 'description', 'duration_days', 'category')
    template_name = 'course_update.html'


class CourseDeleteView(DeleteView):

    model = Course
    template_name = 'course_delete.html'

    def get_success_url(self):
        return reverse('course-list')
    

class AboutView(TemplateView):

    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)