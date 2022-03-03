from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
import core.models


def index(request):
    books = core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books': books})
