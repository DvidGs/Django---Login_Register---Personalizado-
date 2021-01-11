from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_http_methods

from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Users
from .forms import FormularioLogin, FormularioUser
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

'''''@require_http_methods ([ "GET" ,  "POST" ])
#@require_POST
def example(request):
	return HttpResponse('Hello, world. This is the webhook response.')

def Login (request):
	return render(request, 'login.html')

def Register (request):
	return render(request, 'register.html')'''

'''class ListUser(ListView):
    model = Users
    template_name = 'users/listar_usuario.html'

    def get_queryset(self):
        return self.model.object.filter(active=True)             #usuarios que tengo en registro objects

class RegisterUser(CreateView):
    model = Users
    form_class = FormularioUser
    template_name = 'users/crear_usuario.html'
    success_url = reverse_lazy('users:listar_usuarios')       #redireccionar listado de usuarios '''

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = FormularioUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        #form = UserCreationForm()
        form = FormularioUser()
    return render(request, 'registration/register.html', {'form': form})






