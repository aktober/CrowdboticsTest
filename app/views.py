from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from app import forms


class HomePage(generic.View):
    def get(self, request):
        return render(request, 'app/home.html')


class LoginPage(generic.View):
    def get(self, request):
        return render(request, 'app/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(reverse('home'))


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
            perm1 = Permission.objects.get(name='Can change dog')
            perm2 = Permission.objects.get(name='Can delete dog')
            perm3 = Permission.objects.get(name='Can add dog')
            perm4 = Permission.objects.get(name='Can change cat')
            perm5 = Permission.objects.get(name='Can delete cat')
            perm6 = Permission.objects.get(name='Can add cat')
            user.user_permissions.add(perm1, perm2, perm3, perm4, perm5, perm6)
            owner.save()



        return render(request, 'app/register.html', {'registered': True})