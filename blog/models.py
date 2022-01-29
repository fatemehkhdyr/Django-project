import ipaddress
from django.db import models
from django.urls import reverse
from django.utils import timezone
from sqlalchemy import true
from account.models import User
from extentions.utils import jalali_converter
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# define a new manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")

class Category(models.Model):
    parent = models.ForeignKey('self',default=None, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="زیردسته", related_name="children")
    title = models.CharField(max_length=200, verbose_name="موضوع دسته بندی")
    slug = models.SlugField(max_length=100,unique=True, verbose_name=" آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    position = models.IntegerField(verbose_name="جایگاه")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self) -> str:
        return self.title
    
    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('p',"منتشر شده"),
        ('d',"پیش نویس"),
        ('i',"در حال بررسی"),
        ('b',"برگشت داده شده"),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name="نویسنده", related_name="articles")
    title = models.CharField(max_length=200, verbose_name="موضوع مقاله")
    slug = models.SlugField(max_length=100,unique=True, verbose_name="لینک مقاله")
    category = models.ManyToManyField(Category, verbose_name="موضوع", related_name="articles")
    description = models.TextField(verbose_name="محتوا")
    sumbnail_img = models.ImageField(upload_to = "images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default= timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name="آیا مقاله ویژه است ؟")
    status = models.CharField(max_length=1,default='d' , choices=STATUS_CHOICES, verbose_name="وضعیت")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IpAddress, through="ArticleHit",blank=true, related_name="hits", verbose_name="بازدیدها")
    
    def jpublish(self):
        return jalali_converter(self.publish)

    def get_absolute_url(self):
        return reverse("account:home")

    def categorys_to_str(self):
        return", ".join([category.title for category in self.category.active()])
    categorys_to_str.short_description = "موضوع"

    def thumbnail_tag(self):
        return format_html(" <img src={} width='100 height='70> ".format(self.sumbnail_img.url))
    thumbnail_tag.short_description = "عکس"
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self) -> str:
        return self.title
    jpublish.short_description = "زمان انتشار"
    

    objects = ArticleManager()

class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 