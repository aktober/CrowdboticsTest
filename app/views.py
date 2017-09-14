from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from app import forms


class HomePage(generic.View):
    def get(self, request):
        return render(request, 'app/home.html')


class LoginPage(generic.View):
    def get(self, request):
        return HttpResponse('login page')


class RegisterPage(generic.View):
    def get(self, request):
        userForm = forms.UserForm()
        ownerForm = forms.OwnerForm()
        context = {'user': userForm, 'owner': ownerForm}
        return render(request, 'app/register.html', context)

    def post(self, request):
        userForm = forms.UserForm(request.POST)
        ownerForm = forms.OwnerForm(request.POST)

        if userForm.is_valid() and ownerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.is_staff = True
            user.save()

            owner = ownerForm.save(commit=False)
            owner.user = user
            owner.save()

        return render(request, 'app/register.html', {'registered': True})