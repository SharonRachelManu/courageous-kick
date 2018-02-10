# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def createPost(request):
    if request.method == 'GET':
        return render(request, 'createpost.html', {})
    elif request.method == 'POST':
        # save to database
        print(request.POST)
        return render(request, 'createpost.html', {})