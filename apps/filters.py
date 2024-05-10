from django_filters import FilterSet, CharFilter, NumberFilter

from apps.models import Product


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    status = CharFilter(method='filter_status')

    class Meta:
        model = Product
        fields = ['category', 'created_at']

    def filter_status(self, queryset, name, value):
        return queryset.filter(status__name__icontains=value)
