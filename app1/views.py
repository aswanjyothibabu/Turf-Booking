from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.hashers import make_password
from .models import ClientUser,Booking

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def location(request):
    return render (request,'location.html')

def games(request):
    return render (request,'games.html')

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get("password")
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
    if request.user.is_authenticated:
        return redirect("logged")
    return render(request,'login.html')

@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def register(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        place= request.POST.get('place')
        phone= request.POST.get('phone')
        mail= request.POST.get('mail')
        username = request.POST.get('username')
        password = request.POST.get('password')
        ClientUser.objects.create(
            username = username,
            password = make_password(password),
            name=name,
            place=place,
            phone=phone,
            mail=mail,
        )
        return redirect('login')
    if request.user.is_authenticated:
        return redirect('logged')
    return render(request,'signup.html')

@cache_control(no_cache=False, no_store=False, must_revalidate=True)
def logged(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    if request.user.is_authenticated:
        client_user_queryset = ClientUser.objects.get(user_ptr_id=request.user)
        return render(request,'logged.html',context={'client_user':client_user_queryset})
    return redirect('login.html')

def booking(request):
    return render(request,'booking.html')  

def booked(request):

    a = request.POST['game1']
    b = request.POST['date1']
    c= request.POST['time1']
    d = Booking(Game=a,Date_Time=b,Time_Needed=c)
    d.save()
    # return HttpResponse('Successfully Booked') 
    return render(request,'booked.html')
    