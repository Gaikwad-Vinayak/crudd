from sre_constants import SUCCESS
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from .forms import librarymanagement_form,userresi
from .models import librarymanagement_module
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import View
from django.contrib import messages
from .serializers import librarymanagement_module_serilizeres
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth
# Create your views here.

def data(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            dic=librarymanagement_form(request.POST)
            if dic.is_valid():
                usr = request.user
                t = dic.cleaned_data['title']
                c = dic.cleaned_data['category']
                f = dic.cleaned_data['formats']
                l = dic.cleaned_data['location']
                tp = dic.cleaned_data['total_pages']
                data = librarymanagement_module(user=usr,title=t,category=c,formats=f,location=l,total_pages=tp)
                data.save()
                messages.success(request,'data save sucsessfully .')
        else:
            dic=librarymanagement_form()
        return render(request,'core/home.html',{'form':dic})
    return redirect('/accounts/login/')

def show(request):
    data=librarymanagement_module.objects.all()
    return render(request,'core/listofdata.html',{'data':data})

# @method_decorator(login_required, name='dispatch')
class update(UpdateView):
        template_name='core/edit.html'
        model=librarymanagement_module
        fields=['title','category','formats','location','total_pages']
        success_url='/listofdata/'
  
# @method_decorator(login_required, name='dispatch')
class delete(DeleteView):
    model=librarymanagement_module
    success_url='/listofdata/'



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')



class login(LoginView):
    template_name='core/login.html'
    success_url='/'


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')


class customerregistration(View):
    def get(self,request):
        form=userresi()
        return render(request, 'core/registration.html',{'form':form})
    def post(self,request):
        form=userresi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successfully')
            return render(request, 'core/registration.html',{'form':form})
        return render(request, 'core/registration.html',{'form':form})
        
class librarymanagement_module_view(viewsets.ModelViewSet):
    queryset = librarymanagement_module.objects.all()
    serializer_class = librarymanagement_module_serilizeres