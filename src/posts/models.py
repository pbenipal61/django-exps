from djongo import models


class Post(models.Model):
    _id = models.ObjectIdField()
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)
    objects = models.DjongoManager()

    # def __str__(self):
    #     return f"{self.title} - {self.author}"

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    _id = models.ObjectIdField()
    by = models.CharField(max_length=100, blank=False)
    published = models.BooleanField(default=True)
    content = models.TextField()
    post = models.ForeignKey(
        to=Post,
        to_field="_id",
        on_delete=models.CASCADE,
        # validators=[validate_object_id]
    )
    objects = models.DjongoManager()

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     print("here")
    #     self.post = ObjectId(self.post)
    #     super(Comment, self).save(force_insert, force_update, using, update_fields)
