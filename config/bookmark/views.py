from django.shortcuts import render, redirect, get_object_or_404
from models import Bookmark
from .forms import BookmarkForm

# Create your views here.
def list(request):
    list = Bookmark.objects.all()

    return render(request, 'bookmark/list.html',{
        'list': list,
    })