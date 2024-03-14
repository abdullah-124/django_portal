from django.shortcuts import render,redirect
from .forms import AddArticleForm,ReviewForm
from django.contrib.auth.models import User
from .models import Article,Category,Review
from django.http import HttpResponse
from django.db.models import Avg
# Create your views here.
def show_article(req):
    articles = Article.objects.all().order_by('-rating')
    category = Category.objects.all()
    context = {"articles":articles,"category":category}
    return render(req, 'article.html',context)

def article_by_category(req,category_slug=None):
    if(not category_slug):
        articles = Article.objects.all().order_by('-rating')
    else:
        slug_category = Category.objects.get(slug=category_slug)
        articles = Article.objects.filter(category = slug_category).order_by('-rating')
    category = Category.objects.all()
    
    context = {"articles":articles,"category":category}
    
    return render(req,'article.html',context)

def add_article(req):
    if(not req.user.is_authenticated):
        return redirect('login')
    if req.user.has_perm('can_add_article'):
        if(req.method == 'POST'):
            username = req.user.username
            form = AddArticleForm(req.POST, req.FILES)
            if(form.is_valid()):
                author = User.objects.get(username = username)
                article = form.save(commit=False)
                article.author = author
                article.save()
        else :
            form = AddArticleForm()
        return render(req, 'add_article.html', {'form':form})
    return HttpResponse("you have't permission to add article")

def detaile_article(req, id):
    article = Article.objects.get(id = id)
    related_items = Article.objects.exclude(id=id).filter(category = article.category ).order_by('-rating')[:2]
    if(req.method == 'POST'):
        form = ReviewForm(req.POST)
        if(form.is_valid()):
            user = User.objects.get(username = req.user.username)
            review = form.save(commit=False)
            isPosted = Review.objects.filter(user = user ,article=article).exists()
            # print(isPosted)
            if(not isPosted):
                review.user = user
                review.article = article
                review.save()
                article.rating = article.rating_average
                article.save()  
            return redirect('detaile_article',id)
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(article = article)
    # print(reviews)
    
    context ={'article':article, 'releted_items':related_items, "form":form,"reviews":reviews}
    return render(req,'article_detail.html', context)

def delete_article(req,id):
    article = Article.objects.get(id = id)
    if(req.user!=article.author):
        return HttpResponse('<h1>404 bad request</h1>')
    article.delete()
    return redirect('profile')

def edit_article(req,id):
    article = Article.objects.get(id = id)
    if(req.user != article.author):
        return HttpResponse('<h1>404 bad requeset </h1>')
    if(req.method == 'POST'):
        form = AddArticleForm(req.POST, req.FILES, instance=article)
        if(form.is_valid()):
            form.save()
            article.save()
    else:
        form = AddArticleForm(instance=article)
    return render(req,'add_article.html', {'form':form})