from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import *
from .forms import CreateGoods
def Shop(request):
    goods_list = Goods.objects.all()
    paginator = Paginator(goods_list, 4) # Show 25 contacts per page
    page = request.GET.get('page')
    goods = paginator.get_page(page)
    return render(request, 'shop/shop.html', {'goods': goods})

class detail_view(DetailView):
    model = Goods 
    template_name = 'shop/detail_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def form_create_goods(request):
    form = CreateGoods()
    if request.method == "POST":
        form = CreateGoods(request.POST, request.FILES)
        if form.is_valid():
            Goods.objects.create(**form.cleaned_data)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'shop/create_goods.html', context=context)

def contacts(request):
    return render(request, 'shop/contacts.html', {})