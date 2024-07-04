from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
     
    
# category model
# class Category(models.Model):
#     cat_id=models.AutoField(primary_key=True)
#     title=models.CharField(max_length=100)
#     description=models.TextField()
#     url=models.CharField(max_length=100)
#     image=models.ImageField(upload_to='category/')
#     add_date=models.DateTimeField(auto_now_add=True,null=True)
    
class Post(models.Model):
    title=models.CharField(max_length=150)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    
    # class Post(models.Model):
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
    
    
    
class Contact_us(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.email

    
    