from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title
