from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm,ProfileForm, ImageForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from .models import Image, Profile
from django.core.mail import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # profile=Profile(user=user)
            # profile.save()             
            current_site = get_current_site(request)
            mail_subject = 'Activate your instaClown account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you. Now you can login your account.' '<a href="/accounts/login">Click here</a>')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def hello(request):
    images = Image.objects.all()
    return render(request,'instagram/index.html',{"images":images})

@login_required
def view_profile(request,pk):
    current_user = request.user
    profile=User.objects.get(id=pk)
    return render(request, 'instagram/profile.html', {'profile':profile,})

# @login_required(login_url="/accounts/login/")
# def view_profile(request,pk):
#     current_user = request.user
    # profile=Profile.objects.filter(user=request.user.id)
    # images=Image.objects.filter(user=request.user.id)
    # return render (request,'profile.html',{'images':images,'profile':profile,})

@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user=request.user)
    prof_form = ProfileForm()
    if request.method == 'POST':
        prof_form =ProfileForm(request.POST,request.FILES,instance=request.user)
        if prof_form.is_valid:
            prof_form.save()
            return redirect('view_profile/(?P<pk>\d+)')
        else:
            prof_form = ProfileForm()
            # return render(request, 'instagram/edit-profile.html', {"prof_form": prof_form,"profile":profile})
    return render(request, 'instagram/edit-profile.html', {"prof_form": prof_form,"profile":profile})

@login_required(login_url="/accounts/login/")
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form =ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            form.save()
        return redirect('hello')

    else:
        image_form = ImageForm()
    return render(request, 'instagram/upload-image.html', {"image_form": image_form})

@login_required
def search_user(request):
    pass
