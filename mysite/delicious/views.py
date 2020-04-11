from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
from django.template import loader, RequestContext
from . models import  OrderHeader,OrderLine,Dish,SpicyLevel,Contact
import json
from rest_framework import generics
from . serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
def index(request):
    return HttpResponse("Awsome!first page")

def order(request):
    dish= Dish.objects.all()
    spicy=SpicyLevel.objects.all()
    # for s in spicy:
    #     print(s.spice_name)
    #     print(s.id)
    context={'dish':dish}
    context['spicy']=spicy
    return render(request,'order/order.html',context)

def createOrder(request):
    if request.method == 'GET':
        cn = request.GET['customer_name']
        newOrderHeader = OrderHeader(customer_name=cn,creation_time=datetime.datetime.now())
        newOrderHeader.save();
        lastOrder=OrderHeader.objects.all().order_by('pk').first()
        print(lastOrder.order_num)
        res={"order_num":lastOrder.order_num}
        return JsonResponse({"order_num":lastOrder.order_num}, status=200) # Sending an success response
    elif request.method =='POST':
        received_json_data=json.loads(request.body)
        customer_name=received_json_data['customer'];
        order_line=received_json_data['orderLine'];
        print(order_line)
        order_header = OrderHeader(customer_name=customer_name, creation_time=datetime.datetime.now())
        order_header.save();
        for item in order_line:
            order_dish= Dish.objects.get(dish_name=item['dish'])
            order_spicy=SpicyLevel.objects.get(spice_name=item['spicy'])
            order_qty=item['qty']
            order_header.orderline_set.create(dish=order_dish,qty=order_qty,spciy=order_spicy)
        return JsonResponse({"order_num":order_header.order_num}, status=200)  # Sending an success response

def detail(request,order_number):
    print("order number is "+order_number)
    order=OrderHeader.objects.get(order_num=order_number)
    d=order.orderline_set.all()
    for i in d:
        print(i.spicy)
    context = {'orderDetail': order}
    return render(request, 'order/detail.html', context)

@api_view(['GET', 'POST'])
def contact_list(request):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    if request.method == 'GET':

        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    try:
        contact = Contact.objects.get(pk=pk)
    except contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


