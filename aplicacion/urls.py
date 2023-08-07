from django.urls import path
from . import views
from .forms import UsuarioForm, ModeradorForm, JuegoForm

urlpatterns = [
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios_list'),
    path('usuarios/crear/', views.UsuarioCreateView.as_view(), name='crear_usuario'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='detalle_usuario'),
    path('usuarios/<int:pk>/actualizar/', views.UsuarioUpdateView.as_view(), name='actualizar_usuario'),
    path('usuarios/<int:pk>/eliminar/', views.UsuarioDeleteView.as_view(), name='eliminar_usuario'),

    path('moderadores/', views.ModeradorListView.as_view(), name='moderadores_list'),
    path('moderadores/crear/', views.ModeradorCreateView.as_view(), name='crear_moderador'),
    path('moderadores/<int:pk>/', views.ModeradorDetailView.as_view(), name='detalle_moderador'),
    path('moderadores/<int:pk>/actualizar/', views.ModeradorUpdateView.as_view(), name='actualizar_moderador'),
    path('moderadores/<int:pk>/eliminar/', views.ModeradorDeleteView.as_view(), name='eliminar_moderador'),

    path('juegos/', views.JuegoListView.as_view(), name='juegos_list'),
    path('juegos/crear/', views.JuegoCreateView.as_view(), name='crear_juego'),
    path('juegos/<int:pk>/', views.JuegoDetailView.as_view(), name='detalle_juego'),
    path('juegos/<int:pk>/actualizar/', views.JuegoUpdateView.as_view(), name='actualizar_juego'),
    path('juegos/<int:pk>/eliminar/', views.JuegoDeleteView.as_view(), name='eliminar_juego'),
]