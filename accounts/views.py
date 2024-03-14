from django.shortcuts import render,redirect
from .forms import RegestrationForm
from article.models import Article
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if(request.method == 'POST'):
        form = RegestrationForm(request.POST)
        if(form.is_valid()):
            # print(form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect('profile')
    else :
        # print('data not found')
        form = RegestrationForm()
    return render(request,'register.html', {'form':form})

def user_login(request):
    if(request.user.is_authenticated):
        return redirect('home')
    username = request.POST.get('username')
    password = request.POST.get('password')
    # print(username, password)
    user = authenticate(username = username, password = password)
    if(user):
        login(request, user)
        return redirect('profile')
    return render(request, 'login.html')

def user_logout(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect('home')
    return redirect('login')

def profile(req):
    if(req.user.is_authenticated):
        if(req.method == 'POST'):
            form = RegestrationForm(req.POST, instance = req.user)
            if(form.is_valid()):
                form.save()
        else: 
            form = RegestrationForm(instance = req.user)
        
        # article load 
        user = User.objects.get(username = req.user.username)
        articles = Article.objects.filter(author = user).order_by('publishing_time')
        print(articles)
        context = {
            'form':form,
            "articles":articles
        }
        return render(req,'profile.html', context )
    else :
        return redirect('login')