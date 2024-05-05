from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.blogs, name="blogs"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("service/<slug:slug>/", views.service_detail, name="service_detail"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
]
