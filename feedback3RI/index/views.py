from django.shortcuts import render,redirect
from .forms import Visitordetails,SignUpFrom,Feedback
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'aboutus.html')

def contact(request):
    if request.method == "POST":
        c1 = Visitordetails(request.POST)
        if c1.is_valid():
            c1.save()
    else:
        c1 = Visitordetails()
    return render(request,'contactus.html',{'visitor':c1})

def signup(request):
    if request.method == "POST":
        fm = SignUpFrom(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/signin")
    else:
        fm = SignUpFrom()
    return render(request, 'signup.html', {'form': fm})

def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            # feed = FeedbackEntry()
            if user is not None:
                login(request, user)
                # return render(request, 'feedback.html',{'user': user, 'form': feed})
                return redirect("/feedback")

    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'form': fm})

def feedback(request):
    if request.method == "POST":
        f1 = Feedback(request.POST)
        if f1.is_valid():
            f1.save()
    else:
        f1 = Feedback()
    return render(request,"feedback.html",{'feed':f1})

def course(request):
    return render(request,'course.html')

def python(request):
    return render(request,'python.html')

def blockchain(request):
    return render(request,'blockchain.html')

def datascience(request):
    return render(request,'datascience.html')

def selenium(request):
    return render(request,'selenium.html')

def signout(request):
    logout(request)
    return redirect("/signin")
# Create your views here.
