from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'price', 'line_total']

    def validate(self, attrs):
        # Ensure line_total is calculated correctly if not provided
        if attrs.get('line_total') is None:
            attrs['line_total'] = attrs['quantity'] * attrs['price']
        return attrs

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        # Extract details and create the invoice
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        
        # Create InvoiceDetails for the new invoice
        for detail in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail)
        
        return invoice

    def update(self, instance, validated_data):
        # Update the invoice fields
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        # Update or replace the InvoiceDetails
        details_data = validated_data.pop('details')
        
        # Delete existing details first
        instance.details.all().delete()

        # Create new InvoiceDetails
        for detail in details_data:
            InvoiceDetail.objects.create(invoice=instance, **detail)
        
        return instance
