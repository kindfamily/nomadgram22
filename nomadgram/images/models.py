from django.db import models
from nomadgram.users import models as user_models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampedModel):
    """ image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    

class Comment(TimeStampedModel):
    """ Comment Model """
    message = models.TextField()
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)


class Like(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)