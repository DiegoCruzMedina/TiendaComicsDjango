from django.contrib import admin
from .models import Orden, ItemOrden

class ItemOrdenInline(admin.TabularInline):
    model = ItemOrden
    extra = 0

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'total_precio')
    inlines = [ItemOrdenInline]

admin.site.register(Orden, OrdenAdmin)
