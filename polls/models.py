from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    author = models.OneToOneField(User,on_delete= models.CASCADE, null=True )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title


class Coments_1(models.Model):
    post_id = models.ForeignKey(News, on_delete=models.PROTECT, null= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Likes_At_News(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.PROTECT, null = False)
    on_post = models.ForeignKey(News, on_delete=models.PROTECT, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
