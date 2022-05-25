from genericpath import exists
from bleach import clean
from django.shortcuts import redirect, render, redirect, get_object_or_404, reverse

import user
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def thoughts1(request):
    articles = Article.objects.all()

    return render(request,"thoughts1.html",{"articles":articles})

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

@login_required(login_url= "user:login")
def thoughts(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"thoughts.html",context)

@login_required(login_url= "user:login")
def addthought(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article= form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Success!")
        return redirect("index")

    return render(request,"addthought.html",{"form":form})
    
def detail(request,id):
    article = get_object_or_404(Article,id=id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article, "comments":comments})

@login_required(login_url= "user:login")
def update(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance= article)
    if form.is_valid():
        article= form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Success!")
        return redirect("index")

    return render(request,"update.html",{"form":form})

@login_required(login_url= "user:login")
def delete(request,id):
    article = get_object_or_404(Article,id=id)

    article.delete()

    messages.success(request,"Article is successfully deleted!")
    return redirect("article:thoughts")

@login_required(login_url= "user:login")
def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    comment_author = request.user
    if request.method == "POST":
        comment_content = request.POST.get("comment_content")
        
       

    newComment = Comment(comment_author = comment_author ,comment_content = comment_content)

    newComment.article = article

    newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))