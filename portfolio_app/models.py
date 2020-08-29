from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=300)
    image = models.ImageField('portfolio_app/images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title