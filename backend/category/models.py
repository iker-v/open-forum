from django.db import models

class Categories(models.Model):
	name = models.CharField(max_length=60)
	desc = models.TextField()
	image = models.URLField()