from django.shortcuts import render
from django.contrib.auth.models import User
from article.models import Article, Review, Category

def home(request):
    category = Category.objects.all()
    articles = []
    for c in category:
        article = Article.objects.filter(category = c).order_by('-rating')[:2]
        for i in article:
            print(i.headline)
            articles.append(i)
    return render(request, 'home.html', {'articles':articles})

def public_profile(request, username):
    user = User.objects.get(username = username)
    # print(user)
    articles = Article.objects.filter(author = user).order_by('-rating')
    reviews = Review.objects.filter(user = user)
    total = 0
    for i in reviews:
        total += i.rating
    avg = total/len(reviews)
    context = {
        'user':user,
        'articles': articles,
        'avg_rating':avg
    }
    return render(request, 'public_profile.html', context)

def error(req):
    return render(req,'error.html')