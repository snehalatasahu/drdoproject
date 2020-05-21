from django.shortcuts import render, get_object_or_404
from .models import Post, Picture, RecruitmentPost
from .forms import PostForm, RecruitmentPostForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def home(request):
    articles = Post.objects.order_by('-id')
    r_articles = RecruitmentPost.objects.order_by('-id')
    return render(request, 'home.html', {'articles':articles, 'r_articles':r_articles})

def index(request):
    latest_post = Post.objects.latest('id')
    articles = Post.objects.order_by('-id')[1:6]
    r_articles = RecruitmentPost.objects.order_by('-id')
    return render(request, 'index.html', {'post':latest_post, 'articles':articles, 'r_articles':r_articles})

def post_detail(request, slug_text):
    post = Post.objects.filter(slug=slug_text)
    post = post.first()
    articles = Post.objects.exclude(slug=slug_text).order_by('-id')
    r_articles = RecruitmentPost.objects.order_by('-id')
    return render(request, 'index.html', {'post': post, 'articles':articles, 'r_articles':r_articles})

def allArticles(request):
    articles = Post.objects.order_by('-id')
    r_articles = RecruitmentPost.objects.order_by('-id')
    return render(request, 'all_articles.html', {'articles':articles, 'r_articles':r_articles})

def recruitmentArticles(request):
    articles = Post.objects.order_by('-id')
    r_articles = RecruitmentPost.objects.order_by('-id')
    return render(request, 'recruitments.html', {'articles':articles, 'r_articles':r_articles})

def recruitment_post_detail(request, slug_text):
    post = RecruitmentPost.objects.filter(slug=slug_text)
    post = post.first()
    articles = Post.objects.order_by('-id')
    r_articles = RecruitmentPost.objects.exclude(slug=slug_text).order_by('-id')
    return render(request, 'index.html', {'post': post, 'articles':articles, 'r_articles':r_articles})

@staff_member_required
def create_post(request):
    postForm = PostForm()
    files = request.FILES.getlist('images')
    if request.method == 'POST':
        postForm = PostForm(request.POST) 
        if postForm.is_valid():
            postForm.save(commit=True)
            post = Post.objects.latest('id')
            for f in files:
                Picture.objects.create(post=post,pic=f)
            return index(request)

    return render(request, 'create_post.html',{'form':postForm})

@staff_member_required
def create_recruitment_post(request):
    postForm = RecruitmentPostForm()
    if request.method == 'POST':
        postForm = RecruitmentPostForm(request.POST) 
        if postForm.is_valid():
            postForm.save(commit=True)
            return index(request)

    return render(request, 'create_recruitment_post.html',{'form':postForm})

@staff_member_required
def editor(request):
    return render(request, 'editor.html')

