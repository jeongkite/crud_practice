from django.shortcuts import render

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
