from django.urls import path
from django.views.generic import TemplateView

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
    #
    path("blog_detail/", TemplateView.as_view(template_name="web/blog_detail.html"), name="blog_detail"),
    path("customer_stories/", TemplateView.as_view(template_name="web/customer_stories.html"), name="customer_stories"),
    path("service_detail/", TemplateView.as_view(template_name="web/service_detail.html"), name="service_detail"),
]
