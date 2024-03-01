from django.db import models

# Create your models here.
class Catagory(models.Model):
    class Meta:
        verbose_name_plural='catagories'
    def __str__(self):
        return self.catagory_name
    catagory_name=models.CharField(max_length=30)

class Post(models.Model):
    title=models.CharField(max_length=50) 
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_modifie=models.DateTimeField(auto_now=True)
    catagory_name=models.ManyToManyField('Catagory',related_name='posts') 
    def __str__(self):
        return self.title


class Comment(models.Model):
    author=models.CharField(max_length=30)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.author} on '{self.post}'"
