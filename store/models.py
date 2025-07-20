from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="السعر")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="القسم")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
