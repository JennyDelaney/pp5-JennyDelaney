from django.contrib import admin
from .models import Tour, Category


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'duration',
        'price',
        'rating',
        'sku',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Tour, TourAdmin)
admin.site.register(Category, CategoryAdmin)
