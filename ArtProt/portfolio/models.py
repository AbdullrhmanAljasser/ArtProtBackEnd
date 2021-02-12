from django.db import models

# Create your models here.
class Emotions(models.Model):
    id          = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=60)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class ArtImage(models.Model):
    id          = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    motivation  = models.CharField(max_length=150)
    emotion     = models.ForeignKey(Emotions, on_delete=models.SET_NULL, null=True)
    img_url     = models.CharField(max_length=1024)

    def __str__(self):
        return self.title