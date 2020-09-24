from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import datetime
from django.utils import timezone

def get_upload_path(instance, filename):
    return os.path.join(
       "images/{id}/{title}/{file}".format(id=instance.user.id,title=instance.title, file=filename))

def get_upload_path_for_image(instance, filename):
    return os.path.join(
        "images/{id}/{title}/{file}".format(id=instance.auction.user_id, title=instance.auction.title, file=filename))

class User(AbstractUser):
    pass

class Auction(models.Model):
    CHOICES = (
    ('no choice', 'No choice'),
    ('fashion','Fashion'),
    ('tools','Tools'),
    ('toys','Toys'),
    ('electronics','Electronics'),
    ('home accesories','Home accessories'),
    ('books','Books')
)

    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(default="images/default.png",upload_to=get_upload_path)
    category = models.CharField(max_length=64,choices=CHOICES, default="No choice")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    is_active = models.BooleanField(default=True)
    time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc))
    watch_list = models.ManyToManyField(User, blank=True, related_name="follow")


class Image(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, blank=False, null=False, related_name="images")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path_for_image)

    def __str__(self):
        return self.auction.title

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bid")
    starting_bid = models.FloatField()
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Comment(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc))
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'Comment: {self.comment} by: {self.user}'