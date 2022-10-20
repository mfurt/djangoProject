from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Product, Order


class Index(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'


class Detail(DetailView):
    model = Product
    template_name = 'detail.html'


@login_required
def order(request, product_id):
    Order(
        user_id=request.user.id,
        product_id=product_id
    ).save()
    return redirect('/profile')


class UserProfileView(ListView, LoginRequiredMixin):
    login_required()
    template_name = 'profile.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id)
