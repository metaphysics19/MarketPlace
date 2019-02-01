from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Comments
from .models import Category
from .models import Products


def home(request):
    cat = request.GET.get('cat', '')  # αποθηκεύει στην cat το category_id που επιλέξαμε
    txt = request.GET.get('txt', '')  # αποθηκεύει στην txt το κείμενο της Αναζήτησης
    try:
        cat = int(cat)

    except:
        cat = False

    if (cat == False):  # αν δεν έχει επιλεχθεί κατηγορία
        if (txt == ''):  # και αν δεν υπάρχει κείμενο στην Αναζήτηση
            products = Products.objects.filter(date_posted__lte=timezone.now()).order_by('-date_posted')  # εμφανίζει όλα τα προϊόντα που δημοσιεύτηκαν μέχρι σήμερα από το πιο πρόσφατο

        else:  # αν υπάρχει κείμενο στην αναζήτηση, κάνει αναζήτηση στον τίτλο και την περιγραφή του προιόντος
            products = Products.objects.filter(
                (Q(description__contains=txt) | Q(name__contains=txt)) & Q(date_posted__lte=timezone.now())).order_by(
                '-date_posted')

    else:  # εμφανίζει τα προϊόντα της κατηγορίας που επιλέχθηκε
        products = Products.objects.filter(date_posted__lte=timezone.now()).filter(category=cat).order_by(
            '-date_posted')

    # pagination
    page = request.GET.get('page', 1)  # αποθηκεύει στην Page τον αριθμό της σελίδας
    paginator = Paginator(products, 8) # θα εμφανίζει 8 προϊόντα ανά σελίδα
    try:
        products = paginator.page(page)  # εμφανίζει τα προϊόντα της τρέχουσας σελίδας
    except PageNotAnInteger:
        products = paginator.page(1)  # Αν δεν υπάρχει σελίδα να εμφανίζει τα προϊόντα της 1ης
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # Αν είναι άδεια η σελίδα να μην εμφανίζει τίποτα

    categorys = Category.objects.all()  # αποθηκεύει όλες τις κατηγορίες

    return render(request, 'MarketPlace1/home.html', {'products': products, 'categorys': categorys})


class PostListView(ListView):
    model = Products
    template_name = 'MarketPlace1/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_posted']


class ProductsCreateView(CreateView):
    model = Products
    fields = ['name', 'description', 'price', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'MarketPlace1/about.html', {'title': 'About'})


def products_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    categorys = Category.objects.all()
    return render(request, 'MarketPlace1/products_detail.html', {'products': product, 'categorys': categorys}) #καλεί το products_detail.html για το προϊόν που επιλέξαμε


def fill_base(request):
    categories = Category.objects.all()
    return render(request, 'MarketPlace1/base.html', {'categories': categories})

