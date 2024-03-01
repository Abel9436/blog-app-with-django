from django.shortcuts import render
from django.http import HttpResponseRedirect
from BLogapp.models import Catagory,Post,Comment
#from BLogapp.forms import CommentForm
from django import forms

class CommentForm(forms.Form):
    author=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'put your name'}
    ),)
    body=forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'leave your comment here'}
    ),)


# Create your views here.
def blog_index(request):
    post=Post.objects.all().order_by('-created_on')
    context={
        'post':post
    }
    return render(request,'BLogapp/index.html',context)
def blog_catagory(request,catagory):
    post=Post.objects.filter(catagories__name__contains=Catagory).order_by('-created_on')
    context={
        'catagory':catagory,
        'post':post
    }
    return render(request,'BLogapp/catagory.html',context)
def blog_detail(request,pk):
    post=Post.objects.get(pk=pk)
    form=CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    
    comment=Comment.objects.filter(post=post)
    context={
        'post':post,
        'comment':comment,
        'form':CommentForm()
    }
    return render(request,'BLogapp/detail.html',context)