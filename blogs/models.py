from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 70)
    description = models.TextField()
    category = models.CharField(max_length = 20)
    author = models.CharField(max_length = 40)
    published_at =  models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True) 

    def __str__(self) -> str:
        return self.title 