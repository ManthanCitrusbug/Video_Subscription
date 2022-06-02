from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from requests import request
from .forms import AdminRegisterform, LoginForm
from .models import User, Video, Subscription
from django.contrib.auth import authenticate, login, logout
import stripe
from django.conf import settings
from datetime import datetime, timedelta
# Create your views here.

class UserregisterView(CreateView):
    model = User
    form_class = AdminRegisterform
    template_name = 'registration.html'
    success_url = 'login'


class HomePageView(ListView):
    model = Video
    template_name = 'home.html'
    context_object_name = 'videos'


class WatchVideoView(DetailView):
    model = Video
    template_name = 'watch_video.html'


class LoginView(View):
    def post(self,request):
        form = LoginForm(request.POST)
        user_name = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=user_name,password=password)
        if user is not None:
            print(user)
            # if user.is_staff == True:
            login(request, user)
            return redirect('subscription:home')
        else:
            return render(request,'login.html',{'form':form}) 

    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{'form':form})


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('subscription:registraion')


class PaymentView(View):
    def get(self, request):
        return render(request, 'payment.html', {'key':settings.STRIPE_PUBLIC_KEY})

    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        sub_type = request.POST.get('sub_type')
        customer = stripe.Customer.create(
            name = request.user,
            payment_method=request.POST.get('paymentMethodToken'),
            # source = request.POST['stripeToken']
        )
        charge = stripe.PaymentIntent.create(
            customer = customer.id,
            amount=int(sub_type)*100,
            currency='inr',
            payment_method_types=['card'],
        )
        if charge:
            user = User.objects.get(username=request.user)
            sub = Subscription.objects.create(user=request.user)
            print(user)
            if charge.amount == 2400*100:
                user.subscribe = "yearly"
                expiry = datetime.now() + timedelta(days=365)
                sub.expiry_date = expiry
                sub.membership_type = "yearly"
                user.save()
                sub.save()
            if charge.amount == 250*100:
                user.subscribe = "monthly"
                expiry = datetime.now() + timedelta(days=30)
                sub.expiry_date = expiry
                sub.membership_type = "monthly"
                user.save()
                sub.save()
        return redirect('subscription:home')

