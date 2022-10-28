from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def sign_up(request):
    context = {}
    context['title'] = "Sign up | Post Scribers"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse("eroor")

    form = SignUpForm()
    context['form'] = form
    return render(request, 'users/sign_up.html', context)
@login_required
def profile(request):
    context = {}
    context['title'] = "Profile | Post Scribers"
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        Profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if user_form.is_valid() and Profile_form.is_valid():
            user_form.save()
            Profile_form.save()
            return redirect('profile')
    user_form = UserUpdateForm(instance=request.user)
    Profile_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context['user_form'] = user_form
    context['Profile_form'] = Profile_form
    return render(request, 'users/profile.html', context)