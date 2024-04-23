from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to="", null=True, blank=True)
    name = models.CharField("商品名", max_length=100, default="", blank=False)
    price = models.IntegerField("値段", default=0, blank=False)
    created_at = models.DateTimeField("作成日", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("更新日", null=True)

    def __str__(self):
        return self.name
