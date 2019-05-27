from django.contrib import admin
from wait.models import person_information, parameter

#class RestaurantAdmin(admin.ModelAdmin):
#    list_display = ('name', 'phone_number', 'address')
    
#class FoodAdmin(admin.ModelAdmin):
#    list_display = ('name', 'restaurant', 'price')
#    list_filter = ('is_spicy',)
class parameterAdmin(admin.ModelAdmin):
    list_display = ('total_number', 'timeout', 'skip_probability', 'arrive_time', 'average_dining_time', 'table_number')
class person_informationAdmin(admin.ModelAdmin):
    list_display = ('name', 'ID_number', 'place', 'waiting_time')
#admin.site.register(Restaurant,RestaurantAdmin)
#admin.site.register(Food, FoodAdmin)
admin.site.register(person_information, person_informationAdmin)
admin.site.register(parameter, parameterAdmin)