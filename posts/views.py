from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import blog
# Create your views here.
def index(request):
    posts = blog.objects.all()
    return render(request,'index.html',{'posts':posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already used')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username is already taken.....Try another')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password doesn't match")
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if title and content:
            Blog = blog(title = title,detail = content)
            Blog.save()
            return redirect('/')
        else:
            messages.info(request,'All the fields should be filled....')
            return redirect('create')
    return render(request,'create.html')
def post(request,pk):
    posts = blog.objects.get(id=pk)
    return render (request,'post.html',{'posts':posts})