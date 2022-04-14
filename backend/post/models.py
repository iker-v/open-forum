from django.db import models
from django.conf import settings
from thread.models import Threads

class Posts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
