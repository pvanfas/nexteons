from django.shortcuts import render

from .forms import ContactForm
from .models import Blog, Career, Client, FrequentlyAskedQuestion, Product, Service, Slider, Team, Testimonial


def index(request):
    sliders = Slider.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    blogs = Blog.objects.all()[0:3]
    context = {"is_index": True, "sliders": sliders, "services": services, "testimonials": testimonials, "clients": clients, "blogs": blogs}
    return render(request, "web/index.html", context)


def about(request):
    teams = Team.objects.all()
    clients = Client.objects.all()
    context = {"is_about": True, "teams": teams, "clients": clients}
    return render(request, "web/about.html", context)


def blogs(request):
    blogs = Blog.objects.all()
    context = {"is_blogs": True, "blogs": blogs}
    return render(request, "web/blogs.html", context)


def services(request):
    services = Service.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    context = {"is_services": True, "services": services, "faqs": faqs}
    return render(request, "web/services.html", context)


def products(request):
    products = Product.objects.all()
    context = {"is_products": True, "products": products}
    return render(request, "web/products.html", context)


def careers(request):
    careers = Career.objects.all()
    context = {"is_careers": True, "careers": careers}
    return render(request, "web/careers.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = ContactForm()
    context = {"is_contact": True, "form": form}
    return render(request, "web/contact.html", context)
