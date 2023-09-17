from cutomers.models import Customer
from cutomers.serializers import CustomerSerializer
from django.http import JsonResponse

def customers(request):
    # invoke serializer and return to client
    data = Customer.objects.all()
    ser=CustomerSerializer(data, many=True)
    return JsonResponse({'customers':ser.data})