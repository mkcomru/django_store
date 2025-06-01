from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Size"
        verbose_name_plural="Sizes"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
        ordering = ("name",)
        indexes = [models.Index(fields=["name"])]


class ClothingItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    sizes = models.ManyToManyField(Size, through="ClothingItemSize",
                                    related_name='clothing_item', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name='clothing_items')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_price_with_discount(self):
        price = (self.price * (1 - self.discount / 100)) if self.discount else self.price
        return price

    class Meta:
        verbose_name="ClothingItem"
        verbose_name_plural="ClothingItems"


class ClothingItemSize(models.Model):
    clothing_item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return self.clothing_item.name

    class Meta:
        unique_together = ("clothing_item", "size")
        verbose_name="ClothingItemSize"
        verbose_name_plural="ClothingItemSizes"


