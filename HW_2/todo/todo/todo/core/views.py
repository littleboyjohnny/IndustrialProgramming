# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from todo.core.models import todo
# Create your views here.

def index(request):
    items = todo.objects.all()
    return render_to_response('index.html', {'items': items})

def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        td = todo(title=title, text=text)
        td.save()
        return redirect('/')
    else:
        return render(request, 'add.html')
