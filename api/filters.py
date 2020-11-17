from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, BooleanFilter

from api.models import Email


class EmailFilter(filters.FilterSet):
    date = DateTimeFromToRangeFilter()
    sent = BooleanFilter(field_name='sent_date',  lookup_expr='isnull', exclude=True, label="Email Sent?")

    class Meta:
        model = Email
        fields = ['date', 'sent_date', 'sent']
