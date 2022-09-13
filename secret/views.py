from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Team, Folder, Secret

class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['name']
    template_name = 'pages/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.manager = self.request.user
        url = super().form_valid(form)
        return url

class FolderCreate(LoginRequiredMixin, CreateView):
    model = Folder
    fields = ['name', 'description', 'team']
    template_name = 'pages/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        url = super().form_valid(form)
        return url

class SecretCreate(LoginRequiredMixin, CreateView):
    model = Secret
    fields = ['name', 'data', 'folder']
    template_name = 'pages/form.html'
    success_url = reverse_lazy('index')

###################################

class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = ['name']
    template_name = 'pages/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        self.object = get_object_or_404(
            Team,
            manager=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object

class FolderUpdate(LoginRequiredMixin, UpdateView):
    model = Folder
    fields = ['name', 'description']
    template_name = 'pages/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        self.object = get_object_or_404(
            Folder,
            owner=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object
        
class SecretUpdate(LoginRequiredMixin, UpdateView):
    model = Secret
    fields = ['name', 'data', 'folder']
    template_name = 'pages/form.html'
    success_url = reverse_lazy('index')

###################################

class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = 'pages/form-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        self.object = get_object_or_404(
            Team,
            manager=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object

class FolderDelete(LoginRequiredMixin, DeleteView):
    model = Folder
    template_name = 'pages/form-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        self.object = get_object_or_404(
            Folder,
            owner=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object

class SecretDelete(LoginRequiredMixin, DeleteView):
    model = Secret
    template_name = 'pages/form-delete.html'
    success_url = reverse_lazy('index')
