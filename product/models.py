import os.path
from turtle import mode
from django.db import models
from django.contrib.auth.models import User

from markdown import markdown
# from markdownx.models import MarkdownxField
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tags'
    #
    # def get_absolute_url(self):
    #     return f'/blog/tag/{self.slug}'


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    product_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f'[{self.pk}] [{self.name}]'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    # 에러시 return os.path.basename(self.attached_file.name) 로변경
    def get_absolute_url(self):
        return f'/{self.pk}'

    class Meta:
        db_table = 'my_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글'
