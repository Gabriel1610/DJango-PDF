# from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView 
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.models import Group

# Create your views here. 
# https://docs.djangoproject.com/en/4.2/ref/contrib/messages/
# SweeAlert: https://lipis.github.io/bootstrap-sweetalert/)

class RegistrarUsuario (CreateView):
    template_name = 'usuario/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form): #lo soluciono gpt estaba mal en el pdf
        self.object = form.save()  # Guarda el objeto para asegurarse de que no sea None
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name = 'Registrado')
        self.object.groups.add(group)
        form.save()
        return redirect('apps.usuario:registrar')
    
class LoginUsuario(LoginView):
    template_name = 'usuario/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('apps.usuario:login')
    
class LogoutUsuario (LogoutView):
    template_name = 'usuario/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')
        return reverse('apps.usuario:logout')
