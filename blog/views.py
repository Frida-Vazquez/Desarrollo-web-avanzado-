from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Article
from .forms import ArticleForm


@login_required
@permission_required('blog.view_article', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})


@permission_required('blog.add_article', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()

    return render(request, 'blog/article_form.html', {'form': form})


@permission_required('blog.change_article', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/article_form.html', {'form': form})


@permission_required('blog.delete_article', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})


@permission_required('blog.publish_article', raise_exception=True)
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.published = True
    article.save()
    return redirect('article_list')


@permission_required('blog.feature_article', raise_exception=True)
def article_feature(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.featured = True
    article.save()
    return redirect('article_list')