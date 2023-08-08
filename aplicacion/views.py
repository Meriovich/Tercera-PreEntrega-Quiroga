from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Usuario, Moderador, Juego
from .forms import UsuarioForm, ModeradorForm, JuegoForm

class IndexView(TemplateView):
    template_name = 'aplicacion/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuarios_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('aplicacion:usuarios_list')
    template_name = 'usuarios/usuario_confirm_delete.html'


class ModeradorListView(ListView):
    model = Moderador
    template_name = 'moderadores/moderadores_list.html'

class ModeradorDetailView(DetailView):
    model = Moderador
    template_name = 'moderadores/moderador_detail.html'

class ModeradorCreateView(CreateView):
    model = Moderador
    form_class = ModeradorForm
    template_name = 'moderadores/moderador_form.html'

class ModeradorUpdateView(UpdateView):
    model = Moderador
    form_class = ModeradorForm
    template_name = 'moderadores/moderador_form.html'

class ModeradorDeleteView(DeleteView):
    model = Moderador
    success_url = reverse_lazy('moderadores_list')
    template_name = 'moderadores/moderador_confirm_delete.html'


class JuegoListView(ListView):
    model = Juego
    template_name = 'juegos/juegos_list.html'

class JuegoDetailView(DetailView):
    model = Juego
    template_name = 'juegos/juego_detail.html'

class JuegoCreateView(CreateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'juegos/juego_form.html'

class JuegoUpdateView(UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'juegos/juego_form.html'

class JuegoDeleteView(DeleteView):
    model = Juego
    success_url = reverse_lazy('juegos_list')
    template_name = 'juegos/juego_confirm_delete.html'