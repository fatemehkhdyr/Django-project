# Generated by Django 4.0 on 2021-12-30 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='موضوع دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name=' آدرس دسته بندی')),
                ('status', models.BooleanField(verbose_name='وضعیت')),
                ('position', models.IntegerField(verbose_name='جایگاه')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='لینک مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sumbnail_img',
            field=models.ImageField(upload_to='images', verbose_name='تصویر مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='موضوع مقاله'),
        ),
    ]