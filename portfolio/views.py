from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Project


# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


def full_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'full_view.html', context)


class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('index')
    template_name = 'contact.html'
    success_message = 'Your message was submitted successfully'

    def form_invalid(self, form):
        messages.error(self.request, 'An unknown error has occured!')
        return HttpResponseRedirect('')
