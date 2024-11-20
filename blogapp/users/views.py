from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:users-login')
         
    else:
        form = signUpForm ()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)




@login_required
def profile(request):
    return render(request, 'users/profile.html', { 'profile':profile} )




from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm  # Assuming you've created these forms


@login_required
def edit(request):
    if request.method == 'POST':
        # Bind form data to the forms
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        # Validate and save forms
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users:profile')  # Ensure 'profile' is a valid URL name in urls.py
    else:
        # For GET request, instantiate forms with current user data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/edit.html', context)
