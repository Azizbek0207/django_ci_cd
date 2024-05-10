from django_filters import FilterSet, CharFilter, NumberFilter


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    status = CharFilter(method='status_filter')

    def status_filter(self):
        pass