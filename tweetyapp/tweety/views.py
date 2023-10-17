from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CreateUserForm, EditUserForm, UserChangePassword
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

#filtre_liste = ["deprem","enkaz","afetzede"]
#secilen_liste = ["bölge1","bölge2","bölge3"]

# Create your views here.

#sayfalara yönlendirme için
@login_required(login_url='login')
def home(request):
    return render(request, "index.html")

@login_required(login_url='login')
def tyardim(request):
    #tweet = Tweety.objects.all() 
    tweet = Predicted_Tweets.objects.all()   
    context={'tweet':tweet}
    return render(request, "yardim.html",context)

#veri silme
@login_required(login_url='login')
def veriSil(request,pk):
    #tweet = Tweety.objects.get(id=pk) 
    tweet = Predicted_Tweets.objects.get(id=pk) 
    if request.method=="POST":
        tweet.delete()
        return redirect('tyardim')
    context={'item':tweet}
    return render(request, "veri_sil.html",context)

#kullanıcı bilgilerinin güncellenmesi
@login_required(login_url='login')
def user_bilgiler(request):
    msg=None
    if request.method=='POST':
        form=EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = "Bilgiler kaydedildi"
    form=EditUserForm(instance = request.user)
    context={'form':form,'msg':msg}
    return render(request, "user_bilgiler.html", context)

#şifre değiştirme için -> ÇALIŞMIYOR
@login_required(login_url='login')
def change_pwd(request):
    msg=None
    if request.method=='POST':
        new_password=request.POST['new_password']
        updateRes=models.Profile.objects.filter(pk=request.session['userid']).update(pwd=new_password)
        if updateRes:
            del request.session['bilgiler']
            return redirect('bilgiler')
        else:
            msg='Something is wrong!!'
    form = UserChangePassword
    context={'form':form}
    return render(request, 'registration/change_password.html',context)

#kayıt için
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('login')
        context = {'form':form}
        return render(request,'registration/register.html',context)

#giriş için
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not  None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')
        context = {}
        return render(request,'registration/login.html',context)

#kullanıcı çıkışı için
def logoutUser(request):
    logout(request)
    return redirect('login')

