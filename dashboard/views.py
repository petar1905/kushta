from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


def index(request):
  return render(request, 'dashboard.html')
# Create your views here.

def login_page(request):
  next = ''

  if request.GET:
    next = request.GET['next']
  
  if request.POST:
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request,user)
    else:
      return HttpResponseRedirect('/login/error')

    if next == '':
      return HttpResponseRedirect('/')
    else:
      return HttpResponseRedirect(next)

  form = AuthenticationForm()
  context = {'form': form}
  template = loader.get_template('login.html')
  return HttpResponse(template.render(context, request))

def login_error(request):
  return render(request, 'auth_error.html')