from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer

@api_view(['POST', 'PUT'])
def invoice_create_or_update(request):
    if request.method == 'POST':
        # Handle creating a new invoice
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # Handle updating an existing invoice
        invoice_id = request.data.get('id')
        if not invoice_id:
            return Response({"detail": "Invoice ID is required for updating."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            invoice = Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response({"detail": "Invoice not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# created a handle to view the json files as desired
@api_view(['GET'])
def invoice_detail(request, invoice_id):
    try:
        # Retrieve the invoice by ID
        invoice = Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        # Return a 404 if the invoice is not found
        return Response({"detail": "Invoice not found."}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the invoice with its details
    serializer = InvoiceSerializer(invoice)

    return Response(serializer.data, status=status.HTTP_200_OK)
