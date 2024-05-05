from django.db import models

class project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  url = models.URLField(blank=True)
  image = models.ImageField(upload_to='project/images/')

  def __str__(self):
    return self.title
