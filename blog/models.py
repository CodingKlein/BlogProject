#encoding=utf-8

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible   #装饰器
class Category(models.Model):
    """
    Django要求模型必须集成models.Model类
    Category就是一个表名
    name是类的一个属性，代表一个字段
    id列会自动生成
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Tag(models.Model):
    #标签类也是一样
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

 
class Post(models.Model):
    title = models.CharField(max_length=70)
    #标题较短，用CharField储存
    
    body = models.TextField()
    #正文较长，用TextField存储
    
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length = 100, blank = True)

    category = models.ForeignKey(Category)  #一对多
    tags = models.ManyToManyField(Tag, blank = True)   #多对多

    author = models.ForeignKey(User)
    #User是django.contrib.auth内置的应用，专门用来处理网站用户注册，登陆等流程
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def get_category_url(self):
        return reverse('blog:category', kwargs={'pk': self.category.pk})

    def get_tag_url(self):
    	return reverse('blog:tag', kwargs={'pk': self.tags.pk})

    class Meta:
        ordering = ['-created_time']