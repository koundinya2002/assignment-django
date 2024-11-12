from django.urls import path
from .views import invoice_create_or_update, invoice_detail

urlpatterns = [
    path('api/invoices/', invoice_create_or_update, name='invoice_create_or_update'),
    path('api/invoices/<int:invoice_id>/', invoice_detail, name='invoice_detail'),
]