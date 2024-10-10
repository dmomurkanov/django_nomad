from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import Category, Item, ItemImages, ItemParameters


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, TabbedTranslationAdmin,):
    pass

class ItemImagesInline(admin.StackedInline):
    model = ItemImages
    extra = 0

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin, SortableAdminMixin):
    inlines = (ItemImagesInline,)


@admin.register(ItemImages)
class ItemImagesAdmin(admin.ModelAdmin, SortableAdminMixin):
    pass

@admin.register(ItemParameters)
class ItemParametersAdmin(admin.ModelAdmin):
    pass

