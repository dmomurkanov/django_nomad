from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Category, Item, ItemImages
from adminsortable2.admin import SortableAdminMixin

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin, SortableAdminMixin, admin.ModelAdmin):
    pass

class ItemImagesInline(admin.StackedInline):
    model = ItemImages
    extra = 0

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemImagesInline,)


@admin.register(ItemImages)
class ItemImagesAdmin(admin.ModelAdmin):
    pass