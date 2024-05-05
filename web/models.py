from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    top_text = models.CharField(max_length=100)
    main_text = models.CharField(max_length=100)
    description = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=100)

    def __str__(self):
        return self.top_text


class Service(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to="service/")

    def get_absolute_url(self):
        return reverse("web:service_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    image = models.ImageField(upload_to="client/")

    def __str__(self):
        return f"Client {self.id}"


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    summary = models.TextField()
    content = CKEditor5Field("Text", config_name="extends")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def get_absolute_url(self):
        return reverse("web:blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to="team/")
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Product(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")
    content = CKEditor5Field("Content", config_name="extends", blank=True, null=True)
    product_link = models.CharField(max_length=100, blank=True, null=True)
    open_link = models.CharField(max_length=100, choices=(("EXTERNAL", "EXTERNAL WEBSITE"), ("PRODUCT_PAGE", "PRODUCT PAGE")), default="PRODUCT_PAGE")

    def get_absolute_url(self):
        if self.open_link == "EXTERNAL":
            return self.product_link
        return reverse("web:product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
