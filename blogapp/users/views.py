# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from .forms import signUpForm,UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.decorators import login_required

# # Create your views here.



# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator

# def sign_up(request):
#     if request.method == 'POST':
#         form = signUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Do not save to the database yet
#             user.is_active = False  # Deactivate the user until email confirmation
#             user.save()

#             # Generate email confirmation details
#             current_site = get_current_site(request)
#             subject = 'Confirm your email address'
#             message = render_to_string('users/email_confirmation.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': default_token_generator.make_token(user),
#             })
#             send_mail(subject, message, 'salehahmadsarki@gamil.com', [user.email])

#             return redirect('users:users-login')
#     else:
#         form = signUpForm()
    
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/sign_up.html', context)


# # EMAIL Confirmation views
# from django.shortcuts import redirect
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.http import HttpResponse

# def confirm_email(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse("Email confirmed. You can now log in.")
#     else:
#         return HttpResponse("Invalid confirmation link.")

































# @login_required
# def profile(request):
#     return render(request, 'users/profile.html', { 'profile':profile} )




# from django.shortcuts import render, redirect
# from .forms import UserUpdateForm, ProfileUpdateForm  # Assuming you've created these forms


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         # Bind form data to the forms
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
#         # Validate and save forms
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('users:profile')  # Ensure 'profile' is a valid URL name in urls.py
#     else:
#         # For GET request, instantiate forms with current user data
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
    
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request, 'users/edit.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Do not save to the database yet
            user.is_active = False  # Deactivate the user until email confirmation
            user.save()

            # Generate email confirmation details
            current_site = get_current_site(request)
            subject = 'Confirm your email address'
            message = render_to_string('users/email_confirmation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'salehahmadsarki@gamil.com', [user.email])

            # Redirect to a "check your email" page
            return redirect('users:email_sent')
    else:
        form = signUpForm()

    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)


def confirm_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your email has been confirmed. You can now log in.")
        return redirect('users:users-login')  # Redirect to login page
    else:
        messages.error(request, "Invalid confirmation link.")
        return redirect('users:users-login')  # Redirect to login page


def email_sent(request,):
    return render(request,'users/email_sent.html')






@login_required
def profile(request):
    return render(request, 'users/profile.html', {'profile': request.user.profile})


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

