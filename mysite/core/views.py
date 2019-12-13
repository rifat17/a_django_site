from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    count = User.objects.count()
    return render(
        request,
        'home.html',{
        'count':count,
        })


def signup(request):
    print('SIGNUP')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('POST_REQUEST')
        if form.is_valid():
            print('VALID_FORM')
            form.save()
            return redirect('home')
        else:
            print('POST_INVALID')
    else:
        print('GET_REQUEST')
        form = UserCreationForm()

    return render(request=request,
        template_name='registration/signup.html',context={
            'form':form
        })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')



class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'