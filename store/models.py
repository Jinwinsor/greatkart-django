from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # CASCADE => Whenever we want to delete, It'll delete it.
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
# reverse() 함수는 URL 패턴 이름을 사용하여 해당 패턴에 대한 URL을 생성합니다.
# product_detail은 패턴 이름이며, 이 패턴은 category_slug와 product_slug 두 개의 매개변수를 갖습니다.
# 이 매개변수는 args 리스트에 전달됩니다.

    def __str__(self):
        return self.product_name
