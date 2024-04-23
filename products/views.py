from django.views import generic
from products.models import Product


class ProductListView(generic.ListView):
    template_name = 'products/index.html'
    model = Product


class ProductDetailView(generic.DetailView):
    template_name = "products/detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_object_list'] = Product.objects.exclude(pk=self.kwargs.get('pk', ''))
        return context
