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
    #http://127.0.0.1/polls/order
    url(r'^(?P<order_number>[A-Z][0-9]+)/detail', views.detail,name="detail")
    #http://127.0.0.1/poll/123/result

]
