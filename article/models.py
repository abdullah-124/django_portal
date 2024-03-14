from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    slug = models.SlugField(max_length = 30, unique = True)
    image = models.ImageField(upload_to='photos/articles',blank=True)
    def __str__(self) -> str:
        return self.name
 
class Article(models.Model):
    # Headline,Body,Category,Publishing_Time,Ratings
    # author = models.CharField(max_length = 100,blank = True,null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    headline = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='photos/articles',blank=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    rating = models.DecimalField(max_digits = 2, decimal_places=1,default = 0, blank = True)
    @property
    def rating_average(self):
        num = self.review_set.aggregate(models.Avg('rating')).get('rating__avg')
        return num
    
    @property
    def review_count(self):
        return self.review.count()
    

RATING = (
        (1.0, "★☆☆☆☆ (1/5)"),
        (2.0, "★★☆☆☆ (2/5)"),
        (3.0, "★★★☆☆ (3/5)"),
        (4.0, "★★★★☆ (4/5)"),
        (5.0, "★★★★★ (5/5)"),
    )

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, null = True)
    rating = models.DecimalField(max_digits = 2, decimal_places =1, choices = RATING)
    comment = models.CharField(max_length = 200,blank=True,null=True)
    class Meta:
        unique_together = ['user', 'article']

class Portal(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review,on_delete = models.CASCADE, null = True)
