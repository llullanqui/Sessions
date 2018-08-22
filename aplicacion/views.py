from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from aplicacion.models import *
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.
def inicio(request):
	if request.method == "POST":
		usuario = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
		if usuario is not None:
			login(request,usuario)
			response = redirect('pantalla1/')
			response.set_cookie("horaLogin",datetime.datetime.now())
			return response
		else:
			return render(request, 'aplicacion/inicio.html', {"mensaje":"Tu usuario y contraseña no coinciden. Intenta de nuevo."})
	return render(request, 'aplicacion/inicio.html',{"mensaje":""})

def pantalla1(request):
	hora = request.COOKIES.get("horaLogin",0)
	return render(request,'aplicacion/enlaces.html',{"hora":hora})

def pantalla2(request):
	hora = request.COOKIES.get("horaLogin",0)
	return render(request,'aplicacion/contenido.html',{"hora":hora})

def salir(request):
	logout(request)
	return redirect('/')