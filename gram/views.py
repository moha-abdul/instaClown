from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm,ProfileForm, ImageForm, CommentForm
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
            profile=Profile(user=user)
            profile.save()             
            current_site = get_current_site(request)
            # mail_subject = 'Activate your instaClown account.'
            # message = render_to_string('registration/acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]
            # )
            # email.send()
            return HttpResponse('Please confirm your email to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Thank you. Now you can login your account.' '<a href="/accounts/login">Click here</a>')
#     else:
#         return HttpResponse('Activation link is invalid!')

@login_required(login_url="/accounts/login/")
def hello(request):
    images = Image.objects.all()
    co_form = CommentForm()
    return render(request,'instagram/index.html',{"images":images,"co_form": co_form})

# @login_required
# def view_profile(request,pk):
#     current_user = request.user
#     profile=User.objects.get(id=pk)
#     images=Image.objects.filter(id=pk)
#     return render(request, 'instagram/profile.html', {'profile':profile,'images': images})

@login_required
def edit_profile(request):
    images = Image.objects.all()
    profile = Profile.objects.filter(user=request.user)
    current_user = request.user
    photos = Image.objects.filter(user=current_user)
    prof_form = ProfileForm()
    if request.method == 'POST':
        prof_form =ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if prof_form.is_valid:
            prof_form.save()
        else:
            prof_form = ProfileForm()
            return render(request, 'instagram/edit-profile.html', {"image_form": image_form,"photos":photos,"profile":profile,"images":images})
    return render(request, 'instagram/edit-profile.html', {"prof_form": prof_form,"photos":photos,"profile":profile,"images":images})

@login_required(login_url="/accounts/login/")
def view_profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=request.user)
    images=Image.objects.filter(user=request.user)
    return render(request,'instagram/profile.html',{'images':images,'profile':profile,})

# @login_required
# def edit_profile(request):
#     profile = Profile.objects.filter(user=request.user)
#     prof_form = ProfileForm()
#     if request.method == 'POST':
#         prof_form =ProfileForm(request.POST,request.FILES,instance=request.user)
#         if prof_form.is_valid:
#             prof_form.save()
#             return redirect('view_profile/(?P<pk>\d+)')
#         else:
#             prof_form = ProfileForm()
#             # return render(request, 'instagram/edit-profile.html', {"prof_form": prof_form,"profile":profile})
#     return render(request, 'instagram/edit-profile.html', {"prof_form": prof_form,"profile":profile})

@login_required(login_url="/accounts/login/")
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        image_form =ImageForm(request.POST,request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.user = current_user
            image.save()
        return render(request, 'instagram/upload-image.html', {"image_form": image_form})

    else:
        image_form = ImageForm()
    return render(request, 'instagram/upload-image.html', {"image_form": image_form})

@login_required
def new_comment(request,id):
    upload_comment = Image.objects.get(id=id)
    if request.method == 'POST':
        co_form = CommentForm(request.POST)
        if co_form.is_valid():
            comment = co_form.save(commit=False)
            comment.user = request.user
            comment.image= upload_comment
            comment.save()
        return redirect('/')

# @login_required
# def other_profiles(request,id):
#     other_profile = Profile.objects.get(user_id=id)
#     user_images=Image.objects.filter(user_id=id)
                       
#     return render(request,'instagram/other-profile.html',{"other_profile":other_profile,"user_images":user_images})

@login_required
def search_user(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"

        return render(request, 'instagram/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any user"
        return render(request, 'instagram/search.html',{"message":message,"users": searched_users})

@login_required
def single_image(request,project_id):
    image = Image.objects.get(id=project_id)
    return render(request,'instagram/single-image.html',{"image":image})