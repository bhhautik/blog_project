from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session

# Create your views here.

def login(request):
    if request.session.has_key('is_login'):
        return redirect('home')
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        count=User.objects.filter(email=email,password=password).count()
        if count>0:
            request.session['is_login']=True
            request.session['user_id']=User.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('home')
        else:
            messages.error(request,'wrong id password')
        return redirect('login')
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def register_user(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User(username=username,email=email,password=password)
        user.save()
        messages.success(request,'user create successfull')
        return redirect('signup')

def logout(request):
    del request.session['is_login']
    return redirect('login')

def home(request):
    if request.session.has_key('is_login'):
        posts = Post.objects.all
        data=Blog.objects.all
        return render(request,'home.html',{'data':data,'posts':posts})
    return redirect('login')

def viewdetailes(request,id):
    obj=Blog.objects.get(id=id)
    if request.POST:
        message=request.POST['message']
        user_id=request.POST['user_id']
        post_id=id
        query=Comment(message=message)
        query.user_id_id=user_id
        query.post_id_id=post_id
        query.save()
    comment=Comment.objects.all().filter(post_id=id)
    return render(request,'viewdetails.html',{'obj':obj,'comment':comment})

def moredetailes(request,id):
    more=Post.objects.get(id=id)
    photos=Post_image.objects.all
    return render(request,'moreabout.html',{'photos':photos,'more':more})

def create_post(request):
    if request.POST:
        name=request.POST['name']
        title=request.POST['title']
        description=request.POST['description']
        image=request.POST['image']
        obj=Blog(name=name,post_title=title,description=description,image=image)
        obj.save()
        messages.success(request,'your post create succefully')
        return redirect('home')
    return render(request,'create_post.html')



