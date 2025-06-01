from django.contrib import admin
from main.models import Size, ClothingItemSize, \
    ClothingItem, Category


class ClothingItemSizeInline(admin.StackedInline):
    model = ClothingItemSize
    extra = 4


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "available", "price",
                    "discount", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("available", "category")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("-created_at",)
    search_fields = ("name",)
    inlines = [ClothingItemSizeInline]






