from django.db import models
from datetime import date


# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    post_title=models.CharField(max_length=100)
    posted_date=models.DateField(default=date.today)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)

    def __str__(self):
        return self.post_title

class Post(models.Model):
    posttitle=models.CharField(max_length=100)
    disc=models.CharField(max_length=10000)
    image=models.ImageField(blank=True)

class Post_image(models.Model):
    post=models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')

class Comment(models.Model):
    message=models.CharField('message',max_length=1000)
    comment_date=models.DateField(default=date.today)
    post_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)












