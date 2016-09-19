from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SecretManager(models.Manager):
    def like(self, id):
        s = Secret.manager.get(id=id)
        s.likes += 1
        s.save()
        return True
class Secret(models.Model):
    message = models.TextField(max_length=1000)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    manager = SecretManager()
