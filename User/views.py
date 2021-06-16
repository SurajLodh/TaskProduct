from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login, logout
from .models import Post


# Create your views here.

def Home(request):
    return render(request, 'home.html')

def SignUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login')
            else:
                return HttpResponseRedirect('/signup')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})
    
    else:
        return HttpResponseRedirect('/')

def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request = request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login')
            else:
                return HttpResponseRedirect('/login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form' : form})

    else:
        return HttpResponseRedirect('/')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Post_art(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = PostForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user_name = request.user
                instance.save()
                # text = form.cleaned_data['text']
                # post = Post(text = text)
                # post.save()
                # form = PostForm()
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/post')

        else:
            form = PostForm()
            return render(request, 'post.html', {'form' : form})
    else:
        return HttpResponseRedirect('/login')

def Posts_All(request):
    post_s = Post.objects.all()
    return render(request, 'posts.html', {'post_s' : post_s})
