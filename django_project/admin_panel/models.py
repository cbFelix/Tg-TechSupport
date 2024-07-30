from django.db import models


class Message(models.Model):
    content = models.TextField(
        verbose_name="message_content",
        max_length=4096,
    )
    author = models.CharField(
        verbose_name="author_username",
        max_length=128
    )



