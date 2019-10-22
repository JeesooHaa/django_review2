from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed


@require_GET
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


# accounts login 이라 login page 로 감 
# @login_required(login_url='/users/login/')
@login_required
def create(request):
    if request.method == 'POST':
        # Article 을 생성해달라고 하는 요청
        form = ArticleForm(request.POST) # title, content
        # embed()
        if form.is_valid(): # 필드에 적힌 내용만 확인, form 에 없는 NOT NULL 값들은 확인 못함 
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
        # 잘못 입력 되었을 경우 알려줌 
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)
    else: # GET
        # Article 을 생성하기 위한 페이지를 달라고 하는 요청 
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)


@require_GET
def detail(request, article_pk):
    # 사용자가 url 에 적어보낸 article_pk 를 통해 디테일 페이지를 보여준다.
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)
    # 가능
    # return render(request, 'articles/detail.html', {'article': article})


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user == request.user:
        # if request.method == 'POST' and article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article_pk)
        else:
            # 우와
            form = ArticleForm(instance=article)
    else: 
        return redirect('articles:detail', article_pk)
    context = {'form':form}
    return render(request, 'articles/update.html', context)


# 받는 method 를 POST 로 제한 
@require_POST
# POST 로만 오는데 필요한가...
# GET 요청에서만 사용하면됨 
# @login_required
# GET 요청으로 처리하지 말아야 하는 경우에는 사용하면 안됨 login_required
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # if request.method == 'POST':
        if article.user == request.user:
            article.delete()
        else:
            return redirect('articles:detail', article_pk)
        # 보여줄만한 페이지가 따로 없다...
    return redirect('articles:index')


@require_POST
# @login_required
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        # article = get_object_or_404(Article, pk=article_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            # 임시저장 
            comment = form.save(commit=False)
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article_pk)

    # comment = Comment(article_id = article_pk)
    # form = CommentForm(request.POST, instance=comment)
    # form.save()


@require_POST
# @login_required
def comment_delete(request, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        article_pk = comment.article_id
        article = get_object_or_404(Article, pk=article_pk)
        if comment.user == request.user or article.user == request.user:   
            comment.delete()
        return redirect('articles:detail', article_pk)
    # 쿠키를 지우고 접근할때 
    return HttpResponse('You are Unauthorized', status=401)
