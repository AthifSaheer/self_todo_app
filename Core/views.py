from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView
from .models import Text
from .forms import TextForm

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = Text.objects.all()
        return context

class DisplayView(CreateView):
    template_name = "add.html"
    form_class = TextForm
    success_url = '/'

class EditView(UpdateView):
    template_name = "edit.html"
    get_context_data = "edititem"
    model = Text
    fields = "inputfiled"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteView(DeleteView):
    template_name = "delete.html"
    model = Text
    success_url = '/'