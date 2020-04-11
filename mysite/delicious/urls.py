from django.urls import path
from django.conf.urls import url
from . import views
#current path

urlpatterns = [
    path('', views.index,name="index"),
    #http://127.0.0.1/polls
    path("order",views.order, name="order"),
    #http://127.0.0.1/polls/order
    path("createOrder",views.createOrder,name="createOrder"),
    #http://127.0.0.1/delicious/order
    url(r'^(?P<order_number>[A-Z][0-9]+)/detail', views.detail,name="detail"),
    #http://127.0.0.1/delicious/123/detail



    path("api/contacts/",views.contact_list, name="contact_list"),

    #http://127.0.0.1:8000/delicious/api/contacts/
    #if get method list all the object
    #if post method add new object

    path('api/contact/<int:pk>', views.contact_detail,name="contact_detail"),
    #http://127.0.0.1:8000/delicious/api/contact/1(pk)




]
