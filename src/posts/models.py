from djongo import models


class Post(models.Model):
    _id = models.ObjectIdField()
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)
    objects = models.DjongoManager()

    class Meta:
        ordering = ['created']
