from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import (
    Blog,
    BlogCategory,
    Career,
    Client,
    Contact,
    FrequentlyAskedQuestion,
    Product,
    Service,
    Slider,
    Team,
    Testimonial,
)


@admin.register(Slider)
class SliderAdmin(ImportExportActionModelAdmin):
    list_display = ("main_text",)
    search_fields = (
        "top_text",
        "main_text",
        "description",
        "button_text",
        "button_link",
    )


@admin.register(Service)
class ServiceAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "subtitle", "description")
    search_fields = ("icon", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "designation", "description")


@admin.register(Client)
class ClientAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Blog)
class BlogAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Team)
class TeamAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "designation")


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(ImportExportActionModelAdmin):
    list_display = ("question",)
    search_fields = ("question", "answer")


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Career)
class CareerAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")


@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "email", "subject", "phone")
    search_fields = ("name", "email", "subject", "phone", "message")
    readonly_fields = ("name", "email", "subject", "phone", "message")
