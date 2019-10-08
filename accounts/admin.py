from django.contrib import admin

from .models import user, select_food, mon, tue, wed, thu, fri,sat
# Register your models here.
admin.site.register(user)
admin.site.register(select_food)
admin.site.register(mon)  
admin.site.register(tue)
admin.site.register(wed)
admin.site.register(thu)
admin.site.register(fri)
admin.site.register(sat)
