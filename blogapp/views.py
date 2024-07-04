from django.shortcuts import render,HttpResponseRedirect,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm, PostForm,Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,Contact_us
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
# from URLconf.settings import EMAIL_HOST_USER
from django.views.generic import ListView,DetailView
# from .forms import YourModelForm
# Create your views here.

#Home

def home(request):
    posts=Post.objects.all()
    
    return render(request,'blog/home.html',{'posts':posts})

#About
def about(request):
    return render(request,'blog/about.html')
#Contact
def contact(request):
    if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       subject=request.POST.get('subject')
       message=request.POST.get('message')
       contact=Contact_us(
           name=name,
           email=email,
           subject=subject,
           message=message,
        )
    # subject=subject  
    # message=message
    # email_from=settings.EMAIL_HOST_USER
        
    # try:
    #       send_mail(subject,message,email_from,['dubeyaman7070@gmail.com'])
    #       contact.save()
    #       return redirect('home')
    # except:
    #         return redirect('contact')
                   
    return render(request,'blog/contact.html')

     
     
#def Dashbord
def dashbord(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'blog/dashbord.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
    
def Profile(request):
    if request.user.is_authenticated:
        # posts=Post.objects.all()
        # user=request.user
        # full_name=user.get_full_name()
        # gps=user.groups.all()
        return render(request,'blog/profile.html')
    else:
        return HttpResponseRedirect('/login/')
    
#Logout
def user_logout(request):
    logout(request)
    messages.success(request," You were Logged Out !!")
    return redirect('home')
    
#signUp
def user_signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations !! You have become an Author.")
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
      form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

#login
def user_login(request):
    if not request.user.is_authenticated: 
        if request.method == "POST": 
           form=LoginForm(request=request,data=request.POST)
           if form.is_valid():
               uname=form.cleaned_data['username']
               upass=form.cleaned_data['password']
               user=authenticate(username=uname,password=upass)
               if user is not None:
                   login(request,user)
                   messages.success(request,'Logged in Successfully !!')
                   return HttpResponseRedirect('/dashbord/')
        else:
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
       return HttpResponseRedirect('/dashbord/')
   
# Add Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst = Post(title=title , desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request, 'blog/addpost.html', {'form':form})       
    else:
        return HttpResponseRedirect('/login/')
    
#Upadate Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
#delete post
def delete_post(request,id):
        if request.user.is_authenticated:
            if request.method=='POST':
                pi=Post.objects.get(pk=id)
                pi.delete()
                return HttpResponseRedirect('/dashbord/')
        else:
            return HttpResponseRedirect('/login/')
        

    
    