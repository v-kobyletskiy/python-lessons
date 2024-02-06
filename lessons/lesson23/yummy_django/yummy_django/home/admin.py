from django.contrib import admin
from .models import Gallery, Events, Contacts, MenuCategory, MenuDish

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(Contacts)

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuDish)
class MenuDishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
