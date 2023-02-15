from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import (HttpResponseRedirect, JsonResponse)

from django.views.generic.edit import FormView, UpdateView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from .forms import LoginForm
from .models import MyCustomUser
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from apps.cart.models import Cart
from django.template.loader import render_to_string
# Create your views here.


def loginUser(request):
    return render(request, 'login.html')


class LoginView(FormView):
    
    form_class = LoginForm
    template_name  = 'login.html'

    def get(self, request, *args, **kwargs): 
        if request.user.is_authenticated:
            return HttpResponseRedirect('/admin')                                           #redirect if user is logged in
        return super(LoginView, self).get(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        # user = self.request.user
        return ('/')
    
    def post(self, request, *args,**kwargs):
        username = request.POST.get('username')
        try:
            user = MyCustomUser.objects.get(username=username)
        except MyCustomUser.DoesNotExist:
            messages.error(self.request, 'No user found')
            return HttpResponseRedirect('/')
        return super(LoginView, self).post(request, *args, **kwargs)    

    def form_invalid(self, form):
        for key, value in form.errors.items():
            for msg in value:
                messages.error(self.request, f"{key}: {msg}")

        return super(LoginView, self).form_invalid(form)
    
    def form_valid(self, form):
        """ process user login"""
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user is not None:
            if user.is_active:
                login(self.request, user)
                if form.cleaned_data['remember_me']:
                    self.request.session.set_expiry(1209600)
                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.error(self.request, 'Please activate your account.')
        else:
            messages.error(self.request, 'Please check your credentials')

        return HttpResponseRedirect('/')
        #return super(LoginView, self).form_invalid(form)

class home(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
    
        context = super(home, self).get_context_data(**kwargs)
        return context
def Logout(request):
    """logout logged in user"""
    logout(request)
    return HttpResponseRedirect('/login')

def ajax_register(request):
    
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    username = request.GET.get('username')
    password = request.GET.get('password')

    data = {
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'username':username,
        'is_active':True,
    }

    MyCustomUser.objects.create(**data)
    user = MyCustomUser.objects.get(**data)
    
    user.set_password(password)
    user.save()
    
    cart_data = {
        'owner' : user,
        'name': 'Cart'
    }
    #create cart for new user
    Cart.objects.create(**cart_data)

    return JsonResponse({
        'success': True,
    })
