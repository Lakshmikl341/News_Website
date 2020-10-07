from django.shortcuts import render, redirect, HttpResponse
from app_news.models import NewsModel
from .forms import NewsForm

# Create your views here.
def home(request):

    return render(request, "home.html")

def save_news(request):
    form = NewsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
def view_news_one(request, pk):
  news = NewsModel.objects.get(id=pk)

  return render(request, 'view_news_one.html', context={'news': news})
def view_news(request):
    news = NewsModel.objects.all()
    return render(request, "view.html", {"news":news})


def post_news(request):
    news_post = NewsForm()
    return render(request, "post.html", {"news_post":news_post})

def update_news(request, pk):
    news = NewsModel.objects.get(id=pk)

    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect("view_news")
    form = NewsForm(instance=news)
    return render(request, 'update_news.html', context={'form': form})


def delete_news(request, pk):
    news = NewsModel.objects.get(id=pk)
    news.delete()
    return redirect("view_news")