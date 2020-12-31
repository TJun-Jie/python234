from django.shortcuts import render
from .models import User
from . import forms
# Create your views here.

def index(request):
    return render(request, 'appTwo/index.html')


def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = { 'users' : user_list}
    return render(request, 'appTwo/users.html', context=user_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation succesS!")
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text'  + form.cleaned_data['text'])

    return render(request, 'appTwo/form_page.html', {'form': form})