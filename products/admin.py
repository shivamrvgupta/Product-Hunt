from django.contrib import admin
from .models import Product, Vote
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_date', 'Hunter')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'Hunter')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'Hunter')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'hunter', 'product')
    list_display_links = ('id', 'hunter')
    list_per_page = 25


admin.site.register(Vote, VoteAdmin)
