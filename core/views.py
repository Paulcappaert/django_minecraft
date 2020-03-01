from django.shortcuts import render, get_object_or_404
from core.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from mysite.settings import MINECRAFT_SECRET
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account updated')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'core/profile.html', {'form': form})

@csrf_exempt
def confirm(request):
    secret = request.POST['secret']
    mc_username = request.POST['mcusername']
    email = request.POST['email']
    user = get_object_or_404(User, email=email)

    if secret == MINECRAFT_SECRET and user.mc_username == mc_username:
        confirmed_users = User.objects.filter(mc_username=mc_username, is_confirmed=True)
        for other_user in confirmed_users:
            other_user.is_confirmed = False
            other_user.save()

        user.is_confirmed = True
        user.save()

        return HttpResponse('success')

def is_confirmed(request):
    mc_username = request.GET['mcusername']
    confirmed_user = User.objects.filter(mc_username=mc_username, is_confirmed=True)
    if confirmed_user.count():
        result = {'is_confirmed': True}
    else:
        result = {'is_confirmed': False}
    return JsonResponse(result)
