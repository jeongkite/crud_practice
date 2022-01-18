from django.shortcuts import render, get_object_or_404, redirect
from bookmark.forms import CategoryForm, MarkForm

from bookmark.models import Category, Mark

# Create your views here.


def list(request):
    cates = Category.objects.all()
    order_marks = {}
    for c in cates:
        marks = Mark.objects.filter(category=c)
        order_marks[c] = marks
    ctx = {
        'order_marks': order_marks,
    }
    return render(request, 'bookmark/list.html', context=ctx)


def cate_detail(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    marks = cate.mark_set.all()
    ctx = {
        'cate': cate,
        'marks': marks,
    }
    return render(request, 'bookmark/cate_detail.html', context=ctx)


def cate_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            cate = form.save()
            return redirect('bookmark:cate_detail', pk=cate.pk)
    else:
        form = CategoryForm()
    ctx = {
        'form': form,
    }
    return render(request, 'bookmark/form.html', context=ctx)


def cate_edit(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=cate)
        if form.is_valid():
            cate = form.save()
            return redirect('bookmark:cate_detail', pk=cate.pk)
    else:
        form = CategoryForm(instance=cate)
    ctx = {
        'form': form,
    }
    return render(request, 'bookmark/form.html', context=ctx)


def cate_delete(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    cate.delete()
    return redirect('bookmark:list')


def mark_new(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            mark = form.save()
            cate = mark.category
            return redirect('bookmark:cate_detail', pk=cate.pk)
    else:
        form = MarkForm()
    ctx = {
        'form': form
    }
    return render(request, 'bookmark/form.html', context=ctx)


def mark_edit(request, pk):
    mark = get_object_or_404(Mark, pk=pk)
    if request.method == "POST":
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            mark = form.save()
            cate = mark.category
            return redirect('bookmark:cate_detail', pk=cate.pk)
    else:
        form = MarkForm(instance=mark)
    ctx = {
        'form': form
    }
    return render(request, 'bookmark/form.html', context=ctx)


def mark_delete(request, pk):
    mark = get_object_or_404(Mark, pk=pk)
    mark.delete()
    return (redirect('bookmark:list'))
