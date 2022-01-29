from django.contrib import admin
from .models import Article, Category, IpAddress
from django.contrib import messages
from django.utils.translation import ngettext

admin.site.site_header="وبلاگ جنگویی من"

@admin.action(description='اضافه شدن به مقالات منتشر شده.')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
            '%d مقاله به مقالات منتشر شده اضافه شد',
            '%d مقاله به مقالات منتشر شده اضافه شدند.',
            updated,
        ) % updated, messages.SUCCESS)

@admin.action(description='اضافه شدن به مقالات پیش نویس.')
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
            '%d مقاله به مقالات پیش نویس اضافه شد',
            '%d مقاله به مقالات پیش نویس اضافه شدند.',
            updated,
        ) % updated, messages.SUCCESS)

@admin.action(description='فعال کردن وضعیت')
def make_cat_active(modeladmin, request, queryset):
    updated = queryset.update(status=True)
    modeladmin.message_user(request, ngettext(
            '%d دسته بندی به وضعیت فعال تغییر یافت.',
            '%d دسته بندی به وضعیت فعال تغییر یافت.',
            updated,
        ) % updated, messages.SUCCESS)

@admin.action(description='غیرفعال کردن وضعیت ')
def make_cat_deactive(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    modeladmin.message_user(request, ngettext(
            '%d دسته بندی به وضعیت غیرفعال تغییر یافت.',
            '%d دسته بندی به وضعیت غیرفعال تغییر یافت.',
            updated,
        ) % updated, messages.SUCCESS)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status', 'parent','position')
    list_filter = ('status',)
    search_fields = ('title','slug')
    ordering = ['parent__id','status']
    prepopulated_fields  = {'slug':('title',)}
    actions = [make_cat_active, make_cat_deactive]
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'thumbnail_tag','author','jpublish','status','is_special','categorys_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title','description')
    ordering = ['status', 'publish']
    prepopulated_fields  = {'slug':('title',)}
    actions = [make_published, make_draft]

    

    
admin.site.register(Article, ArticleAdmin)
admin.site.register(IpAddress)