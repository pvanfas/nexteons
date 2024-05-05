from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Blog, Career, Client, FrequentlyAskedQuestion, Product, Service, Slider, Team, Testimonial


def index(request):
    sliders = Slider.objects.all()
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    blogs = Blog.objects.all()[0:3]
    context = {"is_index": True, "sliders": sliders, "testimonials": testimonials, "clients": clients, "blogs": blogs}
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
    faqs = FrequentlyAskedQuestion.objects.all()
    context = {"is_services": True, "faqs": faqs}
    return render(request, "web/services.html", context)


def products(request):
    context = {"is_products": True}
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


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {"is_blogs": True, "blog": blog}
    return render(request, "web/blog_detail.html", context)


def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    context = {"is_services": True, "service": service}
    return render(request, "web/service_detail.html", context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        "is_products": True,
        "product": product,
    }
    return render(request, "web/product_detail.html", context)


def view_404(request, exception=None):
    return redirect("/")
