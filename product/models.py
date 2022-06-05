import os.path
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    # image = models.ImageField(upload_to='product/images/', blank=False)

    def __str__(self):
        return f'[{self.pk}] [{self.name}]'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    # 에러시 return os.path.basename(self.attached_file.name) 로변경
    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    class Meta:
        db_table = 'my_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
