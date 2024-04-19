from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", TemplateView.as_view(template_name="web/about.html"), name="about"),
    path("404/", TemplateView.as_view(template_name="web/404.html"), name="404"),
    path("blog_detail/", TemplateView.as_view(template_name="web/blog_detail.html"), name="blog_detail"),
    path("blogs/", TemplateView.as_view(template_name="web/blogs.html"), name="blogs"),
    path("coming_soon/", TemplateView.as_view(template_name="web/coming_soon.html"), name="coming_soon"),
    path("contact/", TemplateView.as_view(template_name="web/contact.html"), name="contact"),
    path("customer_stories/", TemplateView.as_view(template_name="web/customer_stories.html"), name="customer_stories"),
    path("pricing/", TemplateView.as_view(template_name="web/pricing.html"), name="pricing"),
    path("service_detail/", TemplateView.as_view(template_name="web/service_detail.html"), name="service_detail"),
    path("services/", TemplateView.as_view(template_name="web/services.html"), name="services"),
]