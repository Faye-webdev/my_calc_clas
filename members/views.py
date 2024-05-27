from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MembersView(TemplateView):
    template_name = 'myfirst.html'
    extra_context = {'today': datetime.today()}

class AutorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'
    login_url = '/admin'