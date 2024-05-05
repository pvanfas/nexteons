from .models import Product, Service


def main_context(request):
    return {
        "domain": request.META["HTTP_HOST"],
        "services": Service.objects.all(),
        "products": Product.objects.all(),
    }
