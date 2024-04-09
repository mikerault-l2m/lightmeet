from django.template import loader
from django.views.generic import TemplateView
from legal.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

class LegalHome(ListView):
    model = Legal
    context_object_name = "legals"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

class LegalDetail(DetailView):
    model = Legal
    context_object_name = "legal"
    template_name = "legal/legal_detail.html"
    fields = ['title','content','published',]

@method_decorator(login_required,"dispatch")
class LegalCreate(CreateView):
    model = Legal
    template_name = "legal/legal_create.html"
    fields = ['title','content',]

@method_decorator(login_required,"dispatch")
class LegalUpdate(UpdateView):
    model = Legal
    template_name = "legal/legal_edit.html"
    fields = ['title','content','published',]

@method_decorator(login_required,"dispatch")
class LegalDelete(DeleteView):
    model = Legal
    success_url = reverse_lazy("legal_home")
