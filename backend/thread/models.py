import uuid
from django.db import models
from django.conf import settings
from category.models import Categories

class Threads(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	show = models.BooleanField(default=True)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	desc = models.TextField()
	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

class Upvotes(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	thread = models.ForeignKey(Threads, on_delete=models.CASCADE)

class Downvotes(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
