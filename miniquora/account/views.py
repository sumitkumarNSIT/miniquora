from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import CustomUser

# Create your views here.


@require_GET
def base(request):
    if request.user.is_authenticated():
        return redirect('secret')
    f = LoginForm(initial = { 'username' : 'admin'} );
    context = { 'form' : f }
    return render(request, 'base/base.html', context)

@require_POST
def login(request):
    if request.user.is_authenticated():
        return redirect('secret')
    f = LoginForm(request.POST)
    if f.is_valid():
        user = f.get_user();
        auth_login(request, user)
        return redirect('secret')
    else:
        return render(request, 'base/base.html', { 'form': f})

@require_GET
@login_required
def secret(request):
    return HttpResponse('Secret Page');

    
