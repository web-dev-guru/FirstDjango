from django.contrib import admin

# Register your models here.
from .models import Dish,SpicyLevel,OrderHeader,OrderLine,Contact
admin.site.register(Dish)
admin.site.register(SpicyLevel)
admin.site.register(OrderHeader)
admin.site.register(OrderLine)
admin.site.register(Contact)
