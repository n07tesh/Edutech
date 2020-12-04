from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class PostQuery(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    detail = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    slug = models.CharField(max_length=130,default = timezone.now)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' + self.title + " " + 'by' + " " +  self.user.username


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostQuery, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by " + " - " + self.user.username