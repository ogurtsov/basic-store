from django.contrib import admin
from store.models import Category, Item




class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)




class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
