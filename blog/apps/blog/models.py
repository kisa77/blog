from django.db import models

# Create your models here.
class d_posts(models.Model):
    pid = models.IntegerField(max_length=11)
    pTitle = models.CharField(max_length=256)
    pContent = models.TextField()
    pTag = models.CharField(max_length=512)
    pAuthor = models.CharField(max_length=256)
    pMemo = models.CharField(max_length=512)
    pCreated = models.DateTimeField()
    pUpdated = models.DateTimeField()
    pDeleted = models.DateTimeField()
    pStatus = models.IntegerField(max_length=1)

    def __unicode__(self):
         return self.title

    def add_coupon(self) :
        pass
#def add_coupon () :
