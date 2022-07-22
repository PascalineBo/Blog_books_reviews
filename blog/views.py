from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django import forms



@login_required
def home(request):

    return render(request, 'blog/home.html',)