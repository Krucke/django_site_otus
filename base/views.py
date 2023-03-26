from django.views.generic.base import TemplateView

from base.models import Course


class Home(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return self.render_to_response(context)